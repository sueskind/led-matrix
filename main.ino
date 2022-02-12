uint8_t animation;
uint8_t animationsOffset;
uint8_t frame = 0;

void setup() {
  FastLED.addLeds<LED_TYPE, LED_PIN, COLOR_ORDER>(leds, NUM_LEDS);
  FastLED.setBrightness(BRIGHTNESS);

  // start code at random animation
  animationsOffset = random(ANIMATIONS);
}

void loop() {
  // change animation (every 10s) and frame (every loop)
  animation = (millis() / 10000 + animationsOffset) % ANIMATIONS;
  frame = (frame + 1) % frameCounts[animation];

  uint8_t rgb8bit;
  uint8_t r, g, b;
  for (uint8_t i = 0; i < NUM_LEDS; i++){

    // get correct pixel
    rgb8bit = *((uint8_t*)animations[animation] + frame * NUM_LEDS + i);

    // parse colors from 8-bit to 24-bit RGB
    r = (rgb8bit >> 5) * 32;
    g = ((rgb8bit >> 2) % 32) * 32;
    b = (rgb8bit % 4) * 64;

    leds[i].setRGB(r, g, b);
  }

  FastLED.show();

  delay(speeds[animation]);
}
