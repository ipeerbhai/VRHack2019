using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class LeftTreadControl : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        string[] joysticks =  UnityEngine.Input.GetJoystickNames();

    }

    // Update is called once per frame
    void Update()
    {
        // there are two joysticks -- a left and a right.  Each joystick has multiple axes.  I want to use the left thumbstick vertical axis
        // for the left controller.
        var movedY = UnityEngine.Input.GetAxis("LeftThumbstickVertical");


    }
}
