#include "AccelStepper.h"

AccelStepper motor;
void setup()
{
    motor.setMaxSpeed(500);
    motor.setAcceleration(50);
}

void loop()
{
    motor.run();
}