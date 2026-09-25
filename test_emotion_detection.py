import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """
    Unit test for emotion_detector
    """

    def test_joy(self):
        # Joy
        check_1 = emotion_detector("I am glad this happened")
        self.assertEqual(check_1['dominant_emotion'], 'joy')

    def test_anger(self):
        # Anger
        check_2 = emotion_detector("I am really mad about this")
        self.assertEqual(check_2['dominant_emotion'], 'anger')

    def test_disgust(self):
        # Disgust
        check_3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(check_3['dominant_emotion'], 'disgust')

    def test_sad(self):
        # Sad
        check_4 = emotion_detector("I am so sad about this")
        self.assertEqual(check_4['dominant_emotion'], 'sadness')

    def test_fear(self):
        # Fear
        check_5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(check_5['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()