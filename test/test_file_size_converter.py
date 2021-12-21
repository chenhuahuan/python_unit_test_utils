class TestFilesizeConversions(TestCase):

    def test_filesize_conversions(self):
        """Can we convert human filesizes to bytes?"""
        qa_pairs = [
            ('58 kb', 59392),
            ('117 kb', 119808),
            ('117kb', 119808),
            ('1 byte', 1),
            ('117 bytes', 117),
            ('117  bytes', 117),
            ('  117 bytes  ', 117),
            ('117b', 117),
            ('117bytes', 117),
            ('1 kilobyte', 1024),
            ('117 kilobytes', 119808),
            ('0.7 mb', 734003),
            ('1mb', 1048576),
            ('5.2 mb', 5452595),
        ]
        for qa in qa_pairs:
            print("Converting '%s' to bytes..." % qa[0], end='')
            self.assertEqual(convert_size_to_bytes(qa[0]), qa[1])
            print('✓')