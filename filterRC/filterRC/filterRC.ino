#define SIN_OUT 6             //sin wave output (PWM)
#define V_IN A0               //input square wave (PWM signal fro Arduino)
#define V_OUT A1              //output signal (sin wave)

int f = 25;                    //signal's frequency (Hz)
int fs = 100;                 //sampling frequency (Hz)
unsigned int ts = 10;         //sampling time (ms) --> ts=1/fs *1000
int Nsamples;                 //number of samples in a period
int Vout;                     //output voltage to read (sin wave)
int Vin;                      //input square wave to read
int sin_pwm;                  // sin values from 0 to 255


void setup() {
  pinMode(V_IN,INPUT);
  pinMode(V_OUT, INPUT);
  Serial.begin(9600);
  
  Nsamples = 1000 / (f * ts);     //evaluate Nsample to sample the entire sin wave
  //Serial.print(Nsamples);
}

void loop() {
  for (int n = 0; n < Nsamples; n++){
    sin_pwm = 127 * sin( n * (2*PI) / Nsamples ) + 127;    //generate sin signal (from 0 to 254)
    analogWrite(SIN_OUT, sin_pwm);   //write the analog values of sin wave
    Vout = analogRead(V_OUT);        //read signal on pin A1 (sin wave)
    Vin = analogRead(V_IN);          //read signal on pin A0 (square wave)
    Serial.println(Vout);
    //Serial.println(Vin);
    delay(ts);                       //wait before taking the next sample (ms)
  }
  //delay(1000);      //time to wait before each period
}
