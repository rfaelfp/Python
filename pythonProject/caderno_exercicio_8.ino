// Faça com que os leds acendam da direita para a esquerda, de forma cadenciada.
//Aguarde 5 segundos e apague-os da esquerda para a direita, também de forma cadenciada.
void setup() {
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
}

void loop (){
  for(int i = 2; i < 6; i++) {
    digitalWrite(i, HIGH);
    delay(1000);
  }
  delay(5000);
    for(int i = 5; i > 1; i--) {
    digitalWrite(i, LOW);
    delay(1000);
  }
}
