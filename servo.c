#include <Servo.h>
#define numOFValsRec 3
#define digitsPerValRec 3
Servo myservo;
int valsRec[numOFValsRec];
int stringLength = numOFValsRec * digitsPerValRec + 1;
int counter = 0;
bool counterStart = false;
String receivedString;

const int pinBuzzer = 10;
void setup() {
  // put your setup code here, to run once:

  Serial.begin(9600);
  myservo.attach(9);
  myservo.write(90);
  pinMode (pinBuzzer, OUTPUT);
}

void receiveData()
{
  while (Serial.available()) {
    char c = Serial.read();

    if (c == '$') {
      counterStart = true;

    }
    if (counterStart) {

      if (counter < stringLength) {

        receivedString = String (receivedString + c);
        counter++;
      }

      if (counter >= stringLength) {

        for (int i = 0; i < numOFValsRec; i++) {
          int num = (i * digitsPerValRec) + 1;
          valsRec[i] = receivedString.substring(num, num + digitsPerValRec).toInt();

        }

        receivedString = "";
        counter = 0 ;
        counterStart = false;

      }
    }
  }

}



void loop() {
  // put your main code here, to run repeatedly:
  receiveData();
  //if (valsRec[0] == 127) {      // digitalWrite(13, HIGH);
  //}
  //else {

  //digitalWrite(13, LOW);
  //}
  myservo.write(valsRec[0]);
  delay(1000);
  myservo.write(valsRec[1]);
  delay(1000);

  if (valsRec[2] == 255) {
    digitalWrite(10, HIGH);
  }

  else {

    digitalWrite(10, LOW);
  }
}