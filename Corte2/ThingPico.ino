#include <WiFi.h>
#include <ThingSpeak.h>

// Configuración de tu red WiFi
const char* ssid = "POCO M3 Pro 5G";         // ¡Reemplaza con el nombre de tu red WiFi!
const char* password = "plopcetre"; // ¡Reemplaza con la contraseña de tu red WiFi!

// Configuración de ThingSpeak
unsigned long myChannelNumber = 3001186;    // ¡Reemplaza con tu Channel ID de ThingSpeak!
const char* myWriteAPIKey = "W04KBWR7N48EGBTJ";      // ¡Reemplaza con tu Write API Key de ThingSpeak!

// Pin del potenciómetro
const int potenciometroPin = 26;

// Cliente WiFi
WiFiClient client;

void setup() {
  Serial.begin(115200);

  Serial.print("Conectando a ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi conectado!");
  Serial.print("Dirección IP: ");
  Serial.println(WiFi.localIP());

  ThingSpeak.begin(client); // Inicializa la librería ThingSpeak
}

void loop() {
  int valorPotenciometro = analogRead(potenciometroPin); // Lee el valor del potenciómetro

  // Enviar el valor a ThingSpeak
  int statusCode = ThingSpeak.writeField(myChannelNumber, 1, valorPotenciometro, myWriteAPIKey);

  if (statusCode == 200) {
    Serial.print("Envío a ThingSpeak exitoso. Valor: ");
    Serial.println(valorPotenciometro);
  } else {
    Serial.print("Error enviando a ThingSpeak. Código: ");
    Serial.println(statusCode);
  }

  delay(15000); // Envía datos cada 15 segundos (ThingSpeak tiene límites de frecuencia)
}