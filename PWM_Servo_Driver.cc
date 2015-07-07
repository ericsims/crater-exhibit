#include <unistd.h>
#include <stdio.h>
#include <math.h>
#include <wiringPiI2C.h>

class PWM {
 private:
  bool __debug;
  int __address;

 public:
  //Registers
  static const int __MODE1         = 0x00;
  static const int __MODE2         = 0x01;
  static const int __SUBADR1       = 0x02;
  static const int __SUBADR2       = 0x03;
  static const int __SUBADR3       = 0x04;
  static const int __PRESCALE      = 0xFE;
  static const int __LED0_ON_L     = 0x06;
  static const int __LED0_ON_H     = 0x07;
  static const int __LED0_OFF_L    = 0x08;
  static const int __LED0_OFF_H    = 0x09;
  static const int __ALL_LED_ON_L  = 0xFA;
  static const int __ALL_LED_ON_H  = 0xFB;
  static const int __ALL_LED_OFF_L = 0xFC;
  static const int __ALL_LED_OFF_H = 0xFD;

  //Bits
  static const int __RESTART       = 0x80;
  static const int __SLEEP         = 0x10;
  static const int __ALLCALL       = 0x01;
  static const int __INVRT         = 0x10;
  static const int __OUTDRV        = 0x04;

  PWM_Servo_Driver(int address = 0x40, bool debug = false) {
    __debug = debug;
    __address = address;
    if(__debug)
      std::cout << "Reseting PCA9685 MODE1 (without SLEEP) and MODE2" << std::endl;
    setAllPWM(0, 0);
    wiringPiI2CWriteReg8(__address, __MODE2, __OUTDRV);
    wiringPiI2CWriteReg8(__address, __MODE1, __ALLCALL);
    usleep(5);

    int mode1 = wiringPiI2CReadReg8(__address, __MODE1);
    mode1 = mode1 & ~__SLEEP;
    wiringPiI2CWriteReg8(__address, __MODE1, mode1);
    usleep(5);
  }

  void setPWMFreq(float freq) {
    // Set PWM frequency
    float prescaleval = 25000000.0;
    prescaleval /= 4096.0;
    prescaleval /= float(freq);
    prescaleval -= 1.0;
    if(__debug) {
      std::cout << "Setting PWM frequency to " << freq << "Hz" << std::endl;
      std::cout << "Estimated pre-scale: " << prescaleval << std::endl;
    }
    float prescale = floor(prescaleval + 0.5);
    if(__debug)
      std::cout << "Final pre-scale: " << prescale << std::endl;
    int oldmode = wiringPiI2CReadReg8(__address, __MODE1);
    int newmode = (oldmode & 0x7F) | 0x10;
    wiringPiI2CWriteReg8(__address, __MODE1, newmode);
    wiringPiI2CWriteReg8(__address, __PRESCALE, int (floor(prescale)));
    wiringPiI2CWriteReg8(__address, __MODE1, oldmode);
    usleep(5);
    wiringPiI2CWriteReg8(__address, __MODE1, oldmode | 0x80);
  }

  void setPWM(int channel, int on, int off) {
    // Set a single PWM channel
    wiringPiI2CWriteReg8(__address, __LED0_ON_L + 4 * channel, on & 0xFF);
    wiringPiI2CWriteReg8(__address, __LED0_ON_H + 4 * channel, on >> 8);
    wiringPiI2CWriteReg8(__address, __LED0_OFF_L + 4 * channel, off & 0xFF);
    wiringPiI2CWriteReg8(__address, __LED0_OFF_L + 4 * channel, off >> 8);
  }

  void setAllPWM(int on, int off) {
    // Set all PWM channel
    wiringPiI2CWriteReg8(__address, __ALL_LED_ON_L, on & 0xFF);
    wiringPiI2CWriteReg8(__address, __ALL_LED_ON_H, on >> 8);
    wiringPiI2CWriteReg8(__address, __ALL_LED_OFF_L, off & 0xFF);
    wiringPiI2CWriteReg8(__address, __ALL_LED_OFF_H, off >> 8);
  }

};
