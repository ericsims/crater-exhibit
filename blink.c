#include <stdio.h>    // Used for printf() statements
#include <wiringPi.h> // Include WiringPi library!

const int ledPin = 23; // Regular LED - Broadcom pin 23, P1 pin 16

int main(void)
{
    // Setup stuff:
    wiringPiSetupGpio(); // Initialize wiringPi -- using Broadcom pin numbers

    pinMode(ledPin, OUTPUT);     // Set regular LED as output

    printf("blinker is running! Press CTRL+C to quit.");

    while(1)
    {
        // Do some blinking on the ledPin:
        digitalWrite(ledPin, HIGH); // Turn LED ON
        delay(75); // Wait 75ms
        digitalWrite(ledPin, LOW); // Turn LED OFF
        delay(75); // Wait 75ms again
     }

    return 0;
}
