import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )
    
    def test_pelaajaa_ei_loydy(self):
        self.assertAlmostEqual(self.statistics.search("Jaageri"), None)
    
    def test_pelaaja_loytyy(self):
        self.assertAlmostEqual(self.statistics.search("Lemieux").name, "Lemieux")

    def test_etsitaan_joukkueen_pelaajien_lukumaara(self):
        self.assertEqual(len(self.statistics.team("PIT")), 1)
    
    def test_palauttaa_oikeat_pisteporssin_karjen_pelaajat(self):
        pelaajat = self.statistics.top_scorers(2)
        self.assertAlmostEqual(pelaajat[0].name, "Gretzky")
        self.assertAlmostEqual(pelaajat[1].name, "Lemieux")

    def test_palauttaa_oikean_maaran_pelaajia(self):
        self.assertAlmostEqual(len(self.statistics.top_scorers(3)), 3)
    