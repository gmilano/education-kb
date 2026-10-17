<?php
// phpcs:disable moodle.Files.MoodleInternal
// This file is part of Moodle - https://moodle.org/
//
// Moodle is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// Moodle is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with Moodle.  If not, see <https://www.gnu.org/licenses/>.

// phpcs:disable moodle.Files.MoodleInternal
// Standalone CLI tool — not loaded by the Moodle bootstrap.

/**
 * Injects the Moodle GPL license header into PHP, JS, CSS, SCSS and Mustache
 * files that are missing it.
 *
 * Usage: php addheader.php <plugin_dir>
 *
 * @copyright  2026 Jean Lúcio
 * @license    https://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later
 */

if (php_sapi_name() !== 'cli') {
    die("This script must be run from the command line.\n");
}

$targetdir = $argv[1] ?? null;

if (!$targetdir || !is_dir($targetdir)) {
    die("Usage: php addheader.php <plugin_dir>\n");
}

$targetdir = rtrim($targetdir, '/\\');

// Infers the Frankenstyle package name from the path.
$plugintypes = 'block|mod|local|filter|theme|format|auth|enrol|report|tool|qtype|tiny|atto|availability';
if (preg_match('#/(' . $plugintypes . ')/([a-z][a-z0-9_]+)$#', $targetdir, $m)) {
    $package = $m[1] . '_' . $m[2];
} else {
    $package = 'FIXME_' . basename($targetdir);
}

$year = date('Y');

echo "Checking for missing headers in: $targetdir (package: $package)\n\n";

$iterator = new RecursiveIteratorIterator(new RecursiveDirectoryIterator($targetdir));
$filesmodified = 0;
$fileschecked = 0;
$filesskipped = 0;

foreach ($iterator as $file) {
    if (!$file->isFile()) {
        continue;
    }

    $filepath = $file->getPathname();
    $ext = strtolower($file->getExtension());

    $supportedexts = ['php', 'js', 'css', 'scss', 'mustache'];
    if (!in_array($ext, $supportedexts)) {
        continue;
    }

    // Skips minified files and build directories.
    if (
        strpos($filepath, '/amd/build/') !== false ||
        strpos($filepath, '/yui/build/') !== false ||
        strpos($filepath, '/vendor/') !== false ||
        substr_compare($filepath, '.min.js', -7) === 0 ||
        substr_compare($filepath, '.min.css', -8) === 0
    ) {
        continue;
    }

    $content = file_get_contents($filepath);

    if (stripos($content, 'This file is part of Moodle') !== false) {
        $filesskipped++;
        continue;
    }

    $fileschecked++;
    $newcontent = '';

    if ($ext === 'mustache') {
        $header = <<<'MUSTACHE'
{{!
    This file is part of Moodle - https://moodle.org/

    Moodle is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Moodle is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Moodle.  If not, see <https://www.gnu.org/licenses/>.
}}

MUSTACHE;
        $newcontent = $header . $content;
    } else if (in_array($ext, ['css', 'scss'])) {
        // CSS/SCSS: dual GPL + JSDoc block with no blank line between them.
        $header = <<<EOF
/**
 * This file is part of Moodle - https://moodle.org/
 *
 * Moodle is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * Moodle is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with Moodle.  If not, see <https://www.gnu.org/licenses/>.
 */
/**
 * Styles for {$package}.
 *
 * @package    {$package}
 * @copyright  {$year} Jean Lúcio
 * @license    https://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later
 */

EOF;
        $newcontent = $header . $content;
    } else {
        // PHP and JS use the standard // comment block.
        $header = <<<'PHPJS'
// This file is part of Moodle - https://moodle.org/
//
// Moodle is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// Moodle is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with Moodle.  If not, see <https://www.gnu.org/licenses/>.

PHPJS;
        if ($ext === 'php') {
            if (preg_match('/^<\?php\s*/', $content)) {
                $newcontent = preg_replace('/^<\?php\s*/', "<?php\n" . $header, $content, 1);
            } else {
                $newcontent = "<?php\n" . $header . $content;
            }
        } else {
            $newcontent = $header . $content;
        }
    }

    file_put_contents($filepath, $newcontent);
    $relativepath = str_replace($targetdir . '/', '', $filepath);
    echo "[ADDED]   $relativepath\n";
    $filesmodified++;
}

echo "\nDone: $filesskipped already correct, $filesmodified headers added.\n";
