#include <iostream>
#include "PWM_Servo_Driver.cc"

PWM_Servo_Driver pwm;

int main() {
  std::cout << "Hello World!" << std::endl;

  pwm.setPWMFreq(60);
  while(true) {
    pwm.setPWM(0, 0, 150);
    usleep(1000);
    pwm.setPWM(0, 0, 600);
    usleep(1000);
  }
}
