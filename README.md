# Smart-Switch
  
The main purpose of this project is to conntol electrical appliamces while using gestures, In most of the professional spaces there are cameras fixed in some locations, if the electrical appliances, the person who's pointing are are in the visiom of the camera then is application can be used.


When a person points at an electrical appliance and does a specific gesture, the n they get to select that particular applicance and the next gestures performed are directed towards that appliance, the IOT part is achieved with the help of esp-32 and aurdino rely, to demonstrate the project I connected two bulbs and ave themm simple gestures to operate them(on/off).

This project uuses python program whiich updates the values in the realtime datatbase run in firebase, the IOT part- esp-32 uses a wifi module to extract the values of the variables exitsing in the realtime database and send signals the relays to control the electrical appliances based on the logic written in the "setch_smartwitch.io" and the commands will be snet accordingly.

Since the cameras are fixed we maually have to add the coordinates of the appliances, this can alos be autmated by using object detection and extract the co-ordinates of the object, once the input is given we need to run the "new.py" file, thsi file opens the camera and detects when a person is pointing at the particular electrical appliance and cretaes a variable in the realtime database and keeps updating the value based on the gesture detected, so now the appliances are automated and any operation can be cutsomized for a particluar electrical appliance.
