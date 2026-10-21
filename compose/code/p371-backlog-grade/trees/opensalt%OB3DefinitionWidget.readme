Open Badge v3 Definition Widget
===============================

This widget provides a simple form to create an Open Badge v3 achievement
definition.


Usage
-----

The widget can be added to an HTML page by
  1. adding a div element as a placeholder (*ob3-definer* is the default id looked for)
  2. including the javascript and css files from the `dist` folder
  3. dispatching an `ob3-open` custom event
     - Optionally one can pass a selector in the detail of the event to use a different
       div than *#ob3-definer* (see example below)

The widget can be removed from the HTML page by dispatching an `ob3-close` event.

To edit an existing achievement definition, pass the definition as a
JSON string in an attribute called `data-achievement` on the placeholder
div or by adding the JSON (as a string or JSON object) to the detail of the
ob3-open event as the property `achievement`.

To change the default submit button text of "Save", pass the desired
text in an attribute called `data-submit-text` on the placeholder div
or by adding the property `submitText` to the detail of the ob3-open event.

**Note** that the widget does not require the `id` field to be entered
in order for the widget to consider the definition *valid* as many use
cases will require specific types of ids (such as a known URL created
by the application that embeds the widget).


Custom Events
-------------

When the save button is clicked in the widget a `saveDefinition` event
will be triggered with the JSON representation of the achievement
definition as the detail of the event.

When a change is made to a field (and the field is blurred) a `changed`
event will be triggered with a JSON representation of the *possibly
invalid* achievement definition as it currently is entered as the detail
of the event.  This is to allow "autosave" type features to exist in the
application using the widget.

When a change is made to a field (and the field is blurred) and the
definition is currently valid then an `updated` event will be triggered
with a JSON representation of the achievement definition as it currently
is entered as the detail of the event.  This is to allow "autosave"
type features to exist in the application using the widget which expect
the contents to be a valid definition.

The widget is styled using Bootstrap v5 CSS.  To avoid issues with
styling on the rest of the page, it is expected that the Bootstrap CSS
is loaded into the page and thus is not part of the stylesheet provided
with this widget.


Example
-------

Example web page with the widget:
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Achievement Definition Widget</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <script type="module" crossorigin src="/ob3-definer.js"></script>
    <link rel="stylesheet" crossorigin href="/ob3-definer.css">
  </head>
  <body>
    <div id="ob3-definer" data-achievement='{}'></div>
    <script>
      document.addEventListener('DOMContentLoaded', () => {
        window.dispatchEvent(new CustomEvent('ob3-open', {'detail': {'selector': '#ob3-definer'}})); // the detail payload here is optional
      })
    </script>
  </body>
</html>
```

Example JavaScript to capture the event:
```js
window.addEventListener('saveDefinition', function(e) {console.log(e);})
```
