const int sensorPin = A1;
float valorSensor;
float temperaturaC;

void setup() {
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(sensorPin, INPUT);
  Serial.begin(9600);

}
void loop() {
  valorSensor = analogRead(sensorPin);
  temperaturaC = valorSensor / 1024;
  temperaturaC = temperaturaC * 5;
  temperaturaC = temperaturaC - 0.5;
  temperaturaC = temperaturaC * 100;

  Serial.print("Temperatura atual (°C): ");
  Serial.println(temperaturaC);

  if(temperaturaC <= 15) {
    digitalWrite(2, HIGH);
    digitalWrite(3, LOW);
    digitalWrite(4, LOW);
  } else if (temperaturaC <= 24) {
    digitalWrite(2, LOW);
    digitalWrite(3, HIGH);
    digitalWrite(4, LOW);
  } else {
    digitalWrite(2, LOW);
    digitalWrite(3, LOW);
    digitalWrite(4, HIGH);
  }

  delay(1000);
}