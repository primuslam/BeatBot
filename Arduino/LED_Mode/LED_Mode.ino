byte P1 = 3;
byte P2 = 4;
byte P3 = 5;

//Be sure to set these up;

String readString, command;

void setup() {
 Serial.begin(9600);
 pinMode(P1, OUTPUT);
 pinMode(P2, OUTPUT);
 pinMode(P3, OUTPUT);
}

void loop() {
  while (Serial.available()) {
    delay(3); 
    if (Serial.available() >0) {
      char c = Serial.read();
      readString += c;
    }
  }
  
  if (readString.length() > 0) {
    command = readString;
    echo(command);
    act(command);
    readString = "";
  }
}

void echo(String cmd) {
  Serial.println(cmd);
}

void act(String cmd) {
  int control = cmd.toInt();
  if (control >= 100) {
    digitalWrite(P1, HIGH);
    control -= 100;
  }
  if (control >= 10) {
    digitalWrite(P2, HIGH);
    control -= 10;
  }
  if (control >= 1) {
    digitalWrite(P3, HIGH);
  }
  delay(150);
  digitalWrite(P1, LOW);
  digitalWrite(P2, LOW);
  digitalWrite(P3, LOW);  
}
