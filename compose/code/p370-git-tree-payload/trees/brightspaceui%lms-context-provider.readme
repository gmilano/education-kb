# @brightspace-ui/lms-context-provider

Provides LMS context and environment settings to UI components, applications and libraries.

## Installation

Install from NPM:

```shell
npm install @brightspace-ui/lms-context-provider
```

## Usage

### Using a Client

#### Requesting Data

To request data, import `tryGet` from the client and invoke it directly. The first argument should be a context type corresponding to a registered host plugin, while the second argument is an optional set of options to pass through to the host plugin. The third argument is an optional callback to allow a consumer to subscribe to future changes to the data they're requesting.

```js
import { tryGet } from '@brightspace-ui/lms-context-provider/client.js';

const val = await tryGet(
  'my-context-type',
  { someProp: someVal },
  (changedValues) => {
    // This callback should accept a single argument:
    // an object containing any relevant information from the host plugin
	if (changedValues.someChangedProp === 'someVal') {
		doSomeWork(changedValues.someChangedProp);
	}
  }
);
doSomeWork(val);
```

If no host plugin is registered to handle a request, or if the data being requested isn't available, the host will return `undefined`. The host plugin may also need to rely on asynchronous methods to return data, so client code should be resilient to receiving a promise that doesn't resolve or takes some time to resolve.

If no host has been initialized, `tryGet` will reject with an error.

#### Performing an Action

To initiate an action on the host but doesn't require return data, import `tryPerform` from the client and invoke it directly. The first argument should be a context type corresponding to a registered host plugin, while the second argument is an optional set of options to pass through to the host plugin. It is not possible to subscribe to change events using this function.

```js
import { tryPerform } from '@brightspace-ui/lms-context-provider/client.js;'

await tryPerform('my-context-type', { someProp: someVal });
```

If no host plugin is registered to handle a request, or if the data being requested isn't available, this promise will immediately resolve and nothing will happen. As with the `tryGet` function, the host plugin may need to perform asynchronous actions to fulfill a request, so this promise may also never resolve, or may take some time to resolve.

If no host has been initialized, `tryPerform` will reject with an error.

### Configuring a Host

#### Initializing

Initializing a host should rarely be necessary. Within a Brightspace instance, this will generally be handled by BSI via our MVC and legacy frameworks. To initialize a host, import and execute the `initialize` function.

```js
import { initialize } from '@brightspace-ui/lms-context-provider/host.js';

initialize();
```

#### Registering Plugins

To register a host plugin, import and execute the `registerPlugin` function on a page where a host has already been initialized. The provided context type should be unique per page. If a plugin needs to return data to a client, it should provide a `tryGetCallback` as the second argument. If clients can be notified when the data changes, then it should provide a `subscribeCallback` as the third argument.

```js
import { registerPlugin } from '@brightspace-ui/lms-context/provider/host.js';

function tryGetCallback(options) {
	// This can be asynchronous.
	const returnVal = doSomeWork(options);
	return returnVal;
}

function subscribeCallback(onChange, options) {
	// this can be asynchronous.
	const returnVal = doSomeWork(options);

	// Options are defined by the host, not the plugin. sendImmediate indicates the change handler should be invoked immediately.
	if (options.sendImmediate) {
		// Expects an object as its only argument.
		onChange({ val: returnVal });
	}

	// onChange event should be subscribed to future changes.
	registerOnChangeEvent(onChange);
}

registerPlugin('my-context-type', tryGetCallback, subscribeCallback);
```

#### Framed Clients

When working with a client inside an iframe, the host page needs to explicitly allow that iframe. To do this, import and execute `allowFrame` from the host page (the host must already be initialized.). The first argument must be the iframe element itself. The second argument should be the expected origin. Requests from clients within iframes that have not explicitly been allowed or that come from a different origin will be rejected.

```js
import { allowFrame } from '@brightspace-ui/lms-context-provider/host.js';

const myFrame = document.createElement('iframe');
document.body.append(myFrame);

allowFrame(myFrame, window.location.origin);
```

## Developing, Testing and Contributing

After cloning the repo, run `npm install` to install dependencies.

### Linting

```shell
# eslint
npm run lint
```

### Testing

```shell
# run tests
npm test
```

### Versioning and Releasing

This repo is configured to use `semantic-release`. Commits prefixed with `fix:` and `feat:` will trigger patch and minor releases when merged to `main`.

To learn how to create major releases and release from maintenance branches, refer to the [semantic-release GitHub Action](https://github.com/BrightspaceUI/actions/tree/main/semantic-release) documentation.
