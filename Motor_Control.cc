#include <unistd.h>
#include <stdio.h>
#include <math.h>
#include <wiringPiI2C.h>

class StepperMotor {
  private:
    static const int _MICROSTEPS = 8;
    static const int _MICROSTEP_CURVE = [0, 50, 98, 142, 180, 212, 236, 250, 255];
    int _revsteps, _motornum, _sec_per_step, _steppingcounter, _currentstep, _PWMA, _PWMB, _BIN1, _BIN2, _AIN1, _AIN2;
    MotorHAT * MC;
    
    // MICROSTEPS = 16
	  // a sinusoidal curve NOT LINEAR!
    // MICROSTEP_CURVE = [0, 25, 50, 74, 98, 120, 141, 162, 180, 197, 212, 225, 236, 244, 250, 253, 255]

  public:
    Motor_Control(MotorHAT * controller, int num, int steps = 200) {
      MC = &controller;
      _revsteps = steps;
      _motornum = num;
      _sec_per_step = 0.1;
      _steppingcounter = 0;
      _currentstep = 0;
      
      if(num == 1) {
        _PWMA = 8;
        _AIN2 = 9;
        _AIN1 = 10;
        _BIN1 = 11;
        _BIN2 = 12;
        _PWMB = 13;
      } else if(num == 2) {
        _PWMA = 2;
        _AIN2 = 3;
        _AIN1 = 4;
        _BIN1 = 5;
        _BIN2 = 6;
        _PWMB = 7;
      } else {
        // Motor Stepper must be between 1 and 2 inclusive
        return;
      }
    }
    
    void setSpeed(int rpm) {
      _sec_per_step = 60.0 / (_revsteps * rpm);
      _steppingcounter = 0;
    }
    
    void oneStep(int dir, int style) {
      int pwm_a = 255;
      int pwm_b = 255;
      
      if(style == MotorHAT.SINGLE) {
        if((_currentstep / (_MICROSTEPS / 2) % 2) {
          // Odd step
          if(dir == MotorHAT.FORWARD)
            _currentstep += _MICROSTEPS / 2;
          else
            _currentstep -= _MICROSTEP / 2;
        } else {
          // Even step
          if(dir == MotorHAT.FORWARD)
            _currentstep += _MICROSTEPS;
          else
            _currentstep -= _MICROSTEP;
        }
      }
      
      if(style == MotorHAT.DOUBLE) {
        if(!(_currentstep / (_MICROSTEPS / 2) % 2) {
          // Even step
          if(dir == MotorHAT.FORWARD)
            _currentstep += _MICROSTEPS / 2;
          else
            _currentstep -= _MICROSTEPS / 2;
        } else {
          // Odd step
          if(dir == MotorHAT.FORWARD)
            _currentstep += _MICROSTEPS;
          else
            _currentstep -= _MICROSTEP; 
        }
      }
      
      if(style == MotorHAT.INTERLEAVE) {
        if(dir == MotorHAT.FORWARD)
          _currentstep += _MICROSTEPS / 2;
        else
          _currentstep -= _MICROSTEPS / 2;
      }
      
      if(style == MotorHAT.MICROSTEP) {
        if(dir == MotorHAT.FORWARD)
          _currentstep += 1;
        else
          _currentstep -= 1;
        
        // step, then wrap to beginning
        _currentstep += _MICROSTEPS * 4;
        _currentstep %= _MICROSTEPS * 4;
        
        pwm_a = 0;
        pwm_b = 0;
        
        if ((_currentstep >= 0) && (_currentstep < _MICROSTEPS)) {
          pwm_a = _MICROSTEP_CURVE[_MICROSTEPS - _currentstep];
          pwm_b = _MICROSTEP_CURVE[_currentstep];
        } else if((_currentstep >= _MICROSTEPS) && (_currentstep < _MICROSTEPS * 2)) {
          pwm_a = _MICROSTEP_CURVE[_currentstep - _MICROSTEPS];
          pwm_b = _MICROSTEP_CURVE[_MICROSTEPS * 2 - _currentstep];
        } else if((_currentstep >= _MICROSTEPS * 2) && (_currentstep < _MICROSTEPS * 3)) {
          pwm_a = _MICROSTEP_CURVE[_MICROSTEPS * 3 - _currentstep];
          pwm_b = _MICROSTEP_CURVE[_currentstep - _MICROSTEPS * 2];
        } else if((_currentstep >= _MICROSTEPS * 3) && (_currentstep < _MICROSTEPS * 4)) {
          pwm_a = _MICROSTEP_CURVE[_currentstep - _MICROSTEPS * 3];
          pwm_b = _MICROSTEP_CURVE[_MICROSTEPS * 4 - _currentstep];
        }

    }
    
    // step, then wrap to beginning
    _currentstep += _MICROSTEPS * 4;
    _currentstep %= _MICROSTEPS * 4;
    
    MC.
};

class DCMotor {
  
};

class MotorHAT {
  private:
    int _i2caddr, _frequency;
    DCMmotor motors[4];
    StepperMotor steppers[2];
    PWM _pwm;
  
  public:
    enum STYLE { SINGLE, DOUBLE, INTERLEAVE, MICROSTEP };
    enum DIRECTION { FORWARD, DOUBLE, INTERLEAVE, MICROSTEP };
  
    MotorHat(int addr = 0x60, int freq = 1600) {
      _i2caddr = addr;
      _frequency = freq;
      for(int i = 0; i < 4; i++)
        motors[i] = new DCMotor(this, i);
      for(int i = 0; i < 4; i++)
        steppers[i] = new StepperMotor(this, i)
      _pwm = PWM (addr, false);
      _pwm.setPWMFreq(_frequency);
    }
};