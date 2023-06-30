#define SIN_OUT 6             //sin wave output (PWM)
#define V_OUT A0              //output signal (sin wave)

int f = 10 ;                    //signal's frequency (Hz)
int fs = 500;                 //sampling frequency (Hz)
unsigned int ts = 2;         //sampling time (ms) --> ts=1/fs *1000
int Nsamples = 276;                 //number of samples in a period
int Vout;                     //output voltage to read (sin wave)
unsigned long t;
int sin_pwm;                  // sin values from 0 to 255
int t_d;
unsigned long StartTime;

void setup() {
  pinMode(V_OUT, INPUT);
  Serial.begin(9600);
}

void loop() {
  for (int n = 0; n < Nsamples; n++){
    t_d = 1000 / (f * ts);
    sin_pwm = 50 * sin( n * (2*PI) / t_d ) + 50;    //generate sin signal (from 0 to 254)
    analogWrite(SIN_OUT, sin_pwm);   //write the analog values of sin wave
    Vout = analogRead(V_OUT);        //read signal on pin A1 (sin wave)
    if (n == 0) {StartTime=micros();}  //start to count time when the cycle start
    t = micros()-StartTime;
    //Serial.print(t);
    //Serial.print("x");
    Serial.println(Vout);
    //delay(ts);                       //wait before taking the next sample (ms)
  }
  //delay(1000);
  Serial.flush();
}
