// Arduino pin numbers
const int X_pin = 0; // analog pin connected to X output
const int Y_pin = 1; // analog pin connected to Y output
const int SW_pin = 2; // digital pin connected to switch output

void setup() {
  pinMode(SW_pin, INPUT_PULLUP);
  Serial.begin(115200);
}

void loop() {
  Serial.print(analogRead(X_pin));
  Serial.print(", ");
  Serial.print(analogRead(Y_pin));
  Serial.print(", ");
  Serial.print(digitalRead(SW_pin));
  Serial.println();
  delay(50);
}
