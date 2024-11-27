# https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)_per_capita#Table


from decimal import Decimal
from functools import cache

GDP_PER_CAPITA = {
    "MC": Decimal(234317),
    "LI": Decimal(176672),
    "LU": Decimal(133745),
    "BM": Decimal(115750),
    "NO": Decimal(99266),
    "CH": Decimal(93525),
    "KY": Decimal(86863),
    "SG": Decimal(82808),
    "QA": Decimal(81968),
    "IM": Decimal(79531),
    "US": Decimal(76399),
    "IS": Decimal(72902),
    "AU": Decimal(64491),
    "GL": Decimal(57651),
    "SE": Decimal(55873),
    "SM": Decimal(54983),
    "IL": Decimal(54111),
    "AT": Decimal(53840),
    "FI": Decimal(53703),
    "BE": Decimal(51166),
    "DE": Decimal(51073),
    "AE": Decimal(50602),
    "VG": Decimal(49444),
    "HK": Decimal(49259),
    "NZ": Decimal(48249),
    "MO": Decimal(43555),
    "VI": Decimal(39552),
    "GU": Decimal(35905),
    "NC": Decimal(35831),
    "IT": Decimal(35579),
    "PR": Decimal(35209),
    "BN": Decimal(34384),
    "MT": Decimal(33941),
    "KR": Decimal(33147),
    "TW": Decimal(32339),
    "CY": Decimal(32281),
    "SX": Decimal(31210),
    "SI": Decimal(29457),
    "AW": Decimal(29342),
    "BH": Decimal(28464),
    "EE": Decimal(28333),
    "CZ": Decimal(27638),
    "LT": Decimal(24827),
    "PT": Decimal(24651),
    "MF": Decimal(21921),
    "LV": Decimal(21851),
    "SK": Decimal(21390),
    "OM": Decimal(21266),
    "UY": Decimal(20795),
    "GR": Decimal(20867),
    "TC": Decimal(20543),
    "BB": Decimal(20019),
    "PF": Decimal(19957),
    "CK": Decimal(19264),
    "AI": Decimal(19216),
    "GY": Decimal(18990),
    "AG": Decimal(18745),
    "HU": Decimal(18728),
    "HR": Decimal(18413),
    "PL": Decimal(18321),
    "TT": Decimal(18222),
    "KN": Decimal(18158),
    "PA": Decimal(17358),
    "MP": Decimal(17303),
    "CL": Decimal(16265),
    "CW": Decimal(15951),
    "RO": Decimal(15892),
    "SC": Decimal(15875),
    "AS": Decimal(15743),
    "BG": Decimal(13773),
    "AR": Decimal(13297),
    "CR": Decimal(13199),
    "RU": Decimal(13006),
    "PW": Decimal(12084),
    "MY": Decimal(11972),
    "MV": Decimal(11818),
    "NR": Decimal(11757),
    "LC": Decimal(11482),
    "KZ": Decimal(11243),
    "MX": Decimal(11091),
    "TR": Decimal(10616),
    "CU": Decimal(10378),
    "MU": Decimal(10216),
    "GD": Decimal(10016),
    "ME": Decimal(9894),
    "BR": Decimal(9460),
    "RS": Decimal(9394),
    "VC": Decimal(9125),
    "GA": Decimal(8820),
    "TM": Decimal(8508),
    "DM": Decimal(8415),
    "BW": Decimal(7738),
    "IR": Decimal(4388),
    "BA": Decimal(7585),
    "AZ": Decimal(7530),
    "BY": Decimal(7477),
    "PE": Decimal(7126),
    "TH": Decimal(7067),
    "GQ": Decimal(7054),
    "AM": Decimal(7014),
    "BZ": Decimal(6968),
    "AL": Decimal(6803),
    "ZA": Decimal(6777),
    "CO": Decimal(6630),
    "GE": Decimal(6628),
    "MK": Decimal(6600),
    "EC": Decimal(6391),
    "MH": Decimal(6141),
    "JM": Decimal(6047),
    "PY": Decimal(6035),
    "IQ": Decimal(5883),
    "LY": Decimal(5872),
    "SR": Decimal(5667),
    "XK": Decimal(5663),
    "MD": Decimal(5563),
    "GT": Decimal(5407),
    "TV": Decimal(5370),
    "FJ": Decimal(5317),
    "MN": Decimal(4947),
    "ID": Decimal(4788),
    "UA": Decimal(4596),
    "TO": Decimal(4451),
    "DZ": Decimal(4274),
    "JO": Decimal(4205),
    "VN": Decimal(4164),
    "LB": Decimal(4136),
    "WS": Decimal(3919),
    "CV": Decimal(3903),
    "EG": Decimal(3898),
    "MA": Decimal(3853),
    "TN": Decimal(3807),
    "FM": Decimal(3741),
    "BO": Decimal(3523),
    "PH": Decimal(3499),
    "LK": Decimal(3354),
    "DJ": Decimal(3348),
    "VU": Decimal(3073),
    "HN": Decimal(3040),
    "PG": Decimal(2673),
    "BD": Decimal(2621),
    "AO": Decimal(2550),
    "CI": Decimal(2539),
    "ST": Decimal(2486),
    "IN": Decimal(2389),
    "GH": Decimal(2329),
    "SB": Decimal(2285),
    "NI": Decimal(2255),
    "UZ": Decimal(2255),
    "MR": Decimal(2191),
    "KE": Decimal(2099),
    "LA": Decimal(2088),
    "NG": Decimal(2019),
    "HT": Decimal(1748),
    "CM": Decimal(1668),
    "SN": Decimal(1637),
    "KG": Decimal(1607),
    "GN": Decimal(1532),
    "TL": Decimal(1517),
    "ZM": Decimal(1486),
    "KM": Decimal(1485),
    "PK": Decimal(1480),
    "BJ": Decimal(1361),
    "NP": Decimal(1337),
    "MM": Decimal(1096),
    "TJ": Decimal(1054),
    "ET": Decimal(1028),
    "RW": Decimal(966),
    "UG": Decimal(964),
    "TG": Decimal(944),
    "ML": Decimal(875),
    "GM": Decimal(840),
    "SD": Decimal(786),
    "GW": Decimal(776),
    "SY": Decimal(731),
    "TD": Decimal(717),
    "KP": Decimal(654),
    "ER": Decimal(634),
    "YE": Decimal(618),
    "MW": Decimal(613),
    "NE": Decimal(591),
    "MZ": Decimal(542),
    "MG": Decimal(505),
    "SO": Decimal(462),
    "SL": Decimal(461),
    "SS": Decimal(417),
    "AF": Decimal(373),
    "BI": Decimal(246),
    "IE": Decimal(104039),
    "FO": Decimal(69010),
    "DK": Decimal(68037),
    "GB-GSY": Decimal(67961),
    "NLD": Decimal(57871),
    "CAN": Decimal(53247),
    "GB": Decimal(46542),
    "FR": Decimal(44229),
    "AD": Decimal(42066),
    "JP": Decimal(33950),
    "KW": Decimal(32215),
    "BS": Decimal(31458),
    "ES": Decimal(30058),
    "MS": Decimal(16199),
    "CN": Decimal(12541),
    "DO": Decimal(10121),
    "SV": Decimal(5127),
    "NA": Decimal(4836),
    "SZ": Decimal(3995),
    "VE": Decimal(3965),
    "PS": Decimal(3514),
    "BT": Decimal(3266),
    "KH": Decimal(1787),
    "KI": Decimal(1765),
    "ZW": Decimal(1508),
    "TZ": Decimal(1192),
    "LS": Decimal(1107),
    "BF": Decimal(888),
    "LR": Decimal(755),
    "CG": Decimal(2448),
    "CD": Decimal(587),
    "CF": Decimal(461),
}


@cache
def get_gdp(country_code: str) -> Decimal:
    try:
        return GDP_PER_CAPITA[country_code.upper()]
    except KeyError:
        return Decimal(100_000)


@cache
def get_gdp_min() -> Decimal:
    return min(GDP_PER_CAPITA.values())


@cache
def get_gdp_max() -> Decimal:
    return max(GDP_PER_CAPITA.values())