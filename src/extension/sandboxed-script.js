// sandboxed-script.js
if (typeof tf !== 'undefined') {
    console.log('TensorFlow.js is loaded:', tf.version.tfjs);
    // Perform further TensorFlow.js operations here
} else {
    console.error('TensorFlow.js is not loaded');
}
