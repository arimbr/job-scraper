import unittest

from pipelines import format_location, format_description


class TestFormatting(unittest.TestCase):

    def setUp(self):
        self.location_in = "\r\n                    Rotterdam, Nederland\r\n                                    "
        self.location_out = "Rotterdam, Nederland"
        self.description_in = ["\r\n                    ", "\r\n                        Job Description\r\n                    ", "\r\n                ", "Do you have skills in Flash programming and you enjoy working on engaging projects? If the answer is yes then we have the perfect position for you!\u00a0", "\r\n\r\n", "Tasks and\u00a0Responsibilities", "\r\n\r\n", "\r\n", "Participate in the development of technical specifications", "\r\n", "Design, develop and test software in Flash and ActionScript development environment", "\r\n", "Develop and maintain Flash applications based on established specifications, wire-frames and design guidelines", "\r\n", "Carry out unit and integration tests (", "TDD knowledge", ")\u00a0", "\r\n", "Mentor other developers", "\r\n", "Take part in the research of new technologies and solutions", "\r\n", "Work closely together\u00a0with PHP and Front-End developers", "\r\n", "            ", "\r\n", "Expected Qualifications", "\u00a0", "\r\n", "\r\n", "MSC or BSC in Information Technology or equivalent experience", "\r\n", "5+ years of experience in ActionScript programming", "\r\n", "3+ years of experience working with high-availability,\u00a0high-performance, scalable systems", "\r\n", "Strong OOP skills and knowledge of design patterns", "\r\n", "Experience in dynamic content loading, web services/ XML, HTML, and JavaScript", "\r\n", "Knowledge of Unit Testing and Test Driven Development", "\r\n", "Clean Coding is your most important principle", "\r\n", "Ability to think analytically and to\u00a0overview complex systems", "\r\n", "Team player", "\r\n", "Willing to learn and develop themselves", "\r\n", "Follow current technology improvements and recommend their usage in company products if applicable", "\r\n", "Extensive knowledge of Agile methodologies", "\r\n", "Upper intermediate English knowledge (B2)\u00a0or higher", "\r\n", "\r\n", " ", "Advantages", "\r\n", "\r\n", "Experience with Live Streaming and Stream Encoding technologies", "\r\n", "Experience with Adobe FMS and/or Wowza", "\r\n", "Node.js experience", "\r\n", "Familiarity with\u00a0", "Extreme Programming (XP)", "\r\n", "Knowledge of other programming languages\u00a0", "\r\n", "Continuous integration", "\r\n", "                ", "\r\n", "Docler Holding is a multinational enterprise which counts more than 1000 employees worldwide. Created in 2001 and powered by the ideas and visions of young and enthusiastic Hungarian entrepreneurs, today Docler Holding boasts worldwide reach and a global presence. The Group develops and operates world leading websites in the live streaming industry and\u00a0has also created a large number of highly diversified companies which experience ongoing growth in the fields of ICT, media and entertainment.", "\r\n", "\u201cThe driving force behind all our actions is creativity and innovation; regardless of what we are creating - be that a website, a movie, a luxury department store or any other investment\u201d", "\r\n", "- Gy\u00f6rgy Gatty\u00e1n - founder, owner, visionary", "                "]     

    def test_format_location(self):
        self.assertEqual(format_location(self.location_in), self.location_out)

    def test_format_description(self):
        description_out = format_description(self.description_in)
        self.assertIsInstance(description_out, list)
        self.assertIsInstance(description_out[0], str)


if __name__ == '__main__':
    unittest.main()
