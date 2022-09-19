# Mapper4TD

This TouchDesigner container creates and manages networked mappings between input devices and touchdesigner parameters, letting you experiment with creating connections without hardcoding them.

* Supports Python 3.8 and above

## Setup

This setup assumes some familiarity with TD and that the Mapper4TD container is already added to the project.

1. Install libmapper's Python bindings on your computer by typing `pip install libmapper` in your terminal. If you haven't already, add your machine's python search path in TD:
`Edit->Preferences->General->Python 64-bit Module Path`
Set this path to your 'lib/site-packages' directory of your local python installation. Be sure that the python version matches between the 2 installations (check the version in your terminal or TD with `python --version`).

2. Outside of this container, connect any source signals from Touchdesigner to this container's input as a CHOP (Use Merge CHOP if needed). Be sure to name the channels as you want them to show up on the network, and they'll show up in the `inSources` In CHOP.

3. Declare destination signals in the `dstSignalNames` CHOP, then Lock the `dstValues` DAT below it when you're done naming them.

4. Outside of this container, use the outputs to connect to their true destinations.

5. Go up one level and optionally name this container how you'd like the device name to show up on the network. Finally, hit `Re-Init` under the container's Extensions parameter page to set things off.

6. Open webmapper or another mapping UI (http://libmapper.github.io/ecosystem/user_interfaces.html) to form connections with input devices, and have some fun mapping :)