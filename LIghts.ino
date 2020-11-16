const int ch1 = 9;
const int ch2 = 10;
const int ch3 = 11;
int randoColor = 0;
int randoTime = 0;
void setup() {
  // put your setup code here, to run once:
}

void red(){
  digitalWrite(ch1, HIGH);
  delay(randoTime);
  digitalWrite(ch1, LOW);
}
void blue(){
  digitalWrite(ch2, HIGH);
  delay(randoTime);
  digitalWrite(ch2, LOW);
}
void green(){
  digitalWrite(ch3, HIGH);
  delay(randoTime);
  digitalWrite(ch3, LOW);
}
void loop() {
  // put your main code here, to run repeatedly:
  randoTime = random(500,1000);
  green();
  blue();
  red();
}
