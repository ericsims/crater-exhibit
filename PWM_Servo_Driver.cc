class PWM_Servo_Driver {
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

  
};