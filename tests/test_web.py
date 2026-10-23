import unittest
from unittest.mock import patch
from web import build


class EventTest(unittest.TestCase):
    def test_event_change_updates_both_languages_and_calendars(self):
        with patch.dict(build.EVENT, {'start': '2026-10-22T14:15:00+00:00'}):
            for content, date, time in (
                (build.ES, 'Jueves 22 de octubre de 2026', '10:15 a. m.'),
                (build.EN, 'Thursday 22 October 2026', '10:15 a.m.'),
            ):
                with self.subTest(lang=content['lang']):
                    page = build.render(content)
                    long = build.export_text(content)
                    calendar = build.calendar(content).replace('\r\n ', '')
                    self.assertIn(date, page)
                    self.assertIn(date, long)
                    self.assertIn(time, page)
                    metadata = build.event_content(content)['description']
                    self.assertIn(date.lower(), metadata.lower())
                    self.assertIn(time, metadata)
                    self.assertIn('14:15 UTC', page)
                    self.assertIn(time, calendar)
                    self.assertIn('DTSTART:20261022T141500Z', calendar)
                    self.assertIn('DTEND:20261022T151500Z', calendar)
                    self.assertNotIn('9:00', page)
                    self.assertNotIn('9:00', calendar)
                    self.assertNotIn('13:00 UTC', long)

    def test_midnight_and_noon_use_correct_period(self):
        for hour, es, en in ((0, '12:05 a. m.', '12:05 a.m.'),
                             (12, '12:05 p. m.', '12:05 p.m.')):
            with patch.dict(build.EVENT, {'start': f'2026-10-21T{hour:02d}:05:00-04:00'}):
                self.assertIn(es, build.event_chip(build.ES))
                self.assertIn(en, build.event_chip(build.EN))
