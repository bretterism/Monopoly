import logging
from src.tiletype import TileType


class BaseProperty:
    def __init__(self, name, property_value):
        self.name = name
        self.property_owner = 'Bank'
        self.property_value = property_value
        self.mortgage_value = property_value / 2
        self.is_mortgaged = False

    def mortgage_property(self):
        self.is_mortgaged = True
        logging.info(f'Mortgaging property {self.name} for ${self.mortgage_value}')
        return self.mortgage_value

    def update_property_owner(self, owner):
        self.property_owner = owner
        logging.info(f'{owner} now owns property {self.name}.')


class TileProperty(BaseProperty):
    def __init__(self, name, color, property_value,
                 rent, rent_one_house, rent_two_house, rent_three_house, rent_four_house, rent_hotel, cost_per_house):
        super().__init__(name, property_value)

        self.tile_type = TileType.PROPERTY
        self.color = color
        self.rent = {
            0: rent,
            1: rent_one_house,
            2: rent_two_house,
            3: rent_three_house,
            4: rent_four_house,
            5: rent_hotel
        }
        self.cost_per_house = cost_per_house
        self.num_houses = 0

    def get_rent_tile_property(self):
        if self.is_mortgaged:
            return 0

        return self.rent[self.num_houses]

    def add_house(self):
        if self.num_houses < 5:
            self.num_houses += 1
            return self.num_houses
        else:
            return -1

    def mortgage_house(self):
        if self.num_houses > 0:
            self.num_houses -= 1
            logging.info(f'Mortgaging house on property {self.name} for {self.cost_per_house / 2}.')
            return self.cost_per_house / 2
        else:
            return 0


class UtilityProperty(BaseProperty):
    def __init__(self, name):
        super().__init__(name, 150)
        self.tile_type = TileType.UTILITY

    @staticmethod
    def get_rent_by_owner_count(num_properties_owned, dice_roll):
        if num_properties_owned == 1:
            return dice_roll * 4
        elif num_properties_owned == 2:
            return dice_roll * 10

        return 0


class RailroadProperty(BaseProperty):
    def __init__(self, name):
        super().__init__(name, 200)
        self.tile_type = TileType.RAILROAD

    @staticmethod
    def get_rent_by_owner_count(num_properties_owned):
        if 1 <= num_properties_owned <= 4:
            # $25 * 2^(num_properties_owned - 1)
            return 25 * (2 ** (num_properties_owned - 1))

        return 0


def _init_properties():
    return [
        TileProperty(
            name='Mediterranean Avenue',
            color='Purple',
            property_value=60,
            rent=2,
            rent_one_house=10,
            rent_two_house=30,
            rent_three_house=90,
            rent_four_house=160,
            rent_hotel=250,
            cost_per_house=50
        ),
        TileProperty(
            name='Baltic Avenue',
            color='Purple',
            property_value=60,
            rent=4,
            rent_one_house=20,
            rent_two_house=60,
            rent_three_house=180,
            rent_four_house=320,
            rent_hotel=450,
            cost_per_house=50
        ),
        TileProperty(
            name='Oriental Avenue',
            color='Light Blue',
            property_value=100,
            rent=6,
            rent_one_house=30,
            rent_two_house=90,
            rent_three_house=270,
            rent_four_house=4000,
            rent_hotel=550,
            cost_per_house=50
        ),
        TileProperty(
            name='Vermont Avenue',
            color='Light Blue',
            property_value=100,
            rent=6,
            rent_one_house=30,
            rent_two_house=90,
            rent_three_house=270,
            rent_four_house=4000,
            rent_hotel=550,
            cost_per_house=50
        ),
        TileProperty(
            name='Connecticut Avenue',
            color='Light Blue',
            property_value=120,
            rent=8,
            rent_one_house=40,
            rent_two_house=100,
            rent_three_house=300,
            rent_four_house=450,
            rent_hotel=600,
            cost_per_house=50
        ),
        TileProperty(
            name='St. Charles Place',
            color='Pink',
            property_value=140,
            rent=10,
            rent_one_house=50,
            rent_two_house=150,
            rent_three_house=450,
            rent_four_house=625,
            rent_hotel=750,
            cost_per_house=100
        ),
        TileProperty(
            name='States Avenue',
            color='Pink',
            property_value=140,
            rent=10,
            rent_one_house=50,
            rent_two_house=150,
            rent_three_house=450,
            rent_four_house=625,
            rent_hotel=750,
            cost_per_house=100
        ),
        TileProperty(
            name='Virginia Avenue',
            color='Pink',
            property_value=160,
            rent=12,
            rent_one_house=60,
            rent_two_house=180,
            rent_three_house=500,
            rent_four_house=700,
            rent_hotel=900,
            cost_per_house=100
        ),
        TileProperty(
            name='St. James Place',
            color='Orange',
            property_value=180,
            rent=14,
            rent_one_house=70,
            rent_two_house=200,
            rent_three_house=550,
            rent_four_house=750,
            rent_hotel=950,
            cost_per_house=100
        ),
        TileProperty(
            name='Tennessee Avenue',
            color='Orange',
            property_value=180,
            rent=14,
            rent_one_house=70,
            rent_two_house=200,
            rent_three_house=550,
            rent_four_house=750,
            rent_hotel=950,
            cost_per_house=100
        ),
        TileProperty(
            name='New York Avenue',
            color='Orange',
            property_value=200,
            rent=16,
            rent_one_house=80,
            rent_two_house=220,
            rent_three_house=600,
            rent_four_house=800,
            rent_hotel=1000,
            cost_per_house=100
        ),
        TileProperty(
            name='Kentucky Avenue',
            color='Red',
            property_value=220,
            rent=18,
            rent_one_house=90,
            rent_two_house=250,
            rent_three_house=700,
            rent_four_house=870,
            rent_hotel=1050,
            cost_per_house=150
        ),
        TileProperty(
            name='Indiana Avenue',
            color='Red',
            property_value=220,
            rent=18,
            rent_one_house=90,
            rent_two_house=250,
            rent_three_house=700,
            rent_four_house=870,
            rent_hotel=1050,
            cost_per_house=150
        ),
        TileProperty(
            name='Illinois Avenue',
            color='Red',
            property_value=240,
            rent=20,
            rent_one_house=100,
            rent_two_house=300,
            rent_three_house=750,
            rent_four_house=925,
            rent_hotel=1100,
            cost_per_house=150
        ),
        TileProperty(
            name='Atlantic Avenue',
            color='Yellow',
            property_value=260,
            rent=22,
            rent_one_house=110,
            rent_two_house=330,
            rent_three_house=800,
            rent_four_house=975,
            rent_hotel=1150,
            cost_per_house=150
        ),
        TileProperty(
            name='Ventnor Avenue',
            color='Yellow',
            property_value=260,
            rent=22,
            rent_one_house=110,
            rent_two_house=330,
            rent_three_house=800,
            rent_four_house=975,
            rent_hotel=1150,
            cost_per_house=150
        ),
        TileProperty(
            name='Marvin Gardens',
            color='Yellow',
            property_value=280,
            rent=24,
            rent_one_house=120,
            rent_two_house=360,
            rent_three_house=850,
            rent_four_house=1025,
            rent_hotel=1200,
            cost_per_house=150
        ),
        TileProperty(
            name='Pacific Avenue',
            color='Green',
            property_value=300,
            rent=26,
            rent_one_house=130,
            rent_two_house=390,
            rent_three_house=900,
            rent_four_house=1100,
            rent_hotel=1275,
            cost_per_house=200
        ),
        TileProperty(
            name='North Carolina Avenue',
            color='Green',
            property_value=300,
            rent=26,
            rent_one_house=130,
            rent_two_house=390,
            rent_three_house=900,
            rent_four_house=1100,
            rent_hotel=1275,
            cost_per_house=200
        ),
        TileProperty(
            name='Pennsylvania Avenue',
            color='Green',
            property_value=320,
            rent=28,
            rent_one_house=150,
            rent_two_house=450,
            rent_three_house=1000,
            rent_four_house=1200,
            rent_hotel=1400,
            cost_per_house=200
        ),
        TileProperty(
            name='Park Place',
            color='Blue',
            property_value=350,
            rent=35,
            rent_one_house=175,
            rent_two_house=500,
            rent_three_house=1100,
            rent_four_house=1300,
            rent_hotel=1500,
            cost_per_house=200
        ),
        TileProperty(
            name='Boardwalk',
            color='Blue',
            property_value=400,
            rent=50,
            rent_one_house=200,
            rent_two_house=600,
            rent_three_house=1400,
            rent_four_house=1700,
            rent_hotel=2000,
            cost_per_house=200
        ),
        UtilityProperty(name='Electric Company'),
        UtilityProperty(name='Water Works'),
        RailroadProperty(name='Reading Railroad'),
        RailroadProperty(name='Pennsylvania Railroad'),
        RailroadProperty(name='B. & O. Railroad'),
        RailroadProperty(name='Short Line')
    ]


class Properties:
    properties = _init_properties()

    @staticmethod
    def get_properties(tile_type=None):
        if tile_type:
            return [p for p in Properties.properties if p.tile_type == tile_type]
        else:
            return Properties.properties

    @staticmethod
    def get_property_by_name(property_name):
        for idx, prop in enumerate(Properties.properties):
            if property_name == prop.name:
                return Properties.properties[idx]

    @staticmethod
    def get_property_owner_by_name(tile_name):
        prop = Properties.get_property_by_name(tile_name)
        if not prop:
            raise Exception('Could not find property ' + tile_name)

        return prop.property_owner

    @staticmethod
    def get_properties_by_owner(owner_name, tile_type=None, color=None):
        all_props = []
        for p in Properties.properties:
            if p.property_owner == owner_name:
                all_props.append(p)

        if color and (tile_type != TileType.PROPERTY):
            raise Exception('Cannot use color param unless also using TileType.PROPERTY')

        if color and (tile_type == TileType.PROPERTY):
            props = [p for p in all_props if p.tile_type == tile_type and p.color == color]
        elif tile_type and not color:
            props = [p for p in all_props if p.tile_type == tile_type]
        else:
            props = all_props

        return props

    @staticmethod
    def get_property_names_by_owner(owner_name, tile_type=None):
        properties_owned = Properties.get_properties_by_owner(owner_name, tile_type)
        return [p.name for p in properties_owned]

    @staticmethod
    def get_rent(property_name, dice_roll):
        # Rent is calculated differently based on property type (Regular, Railroads, Utilities)
        prop = Properties.get_property_by_name(property_name)

        # If bank owns property, no rent is due.
        if prop.property_owner == 'Bank':
            return 0

        if prop.tile_type == TileType.PROPERTY:
            property_colors = Properties.get_properties_by_color(prop.color)
            rent = prop.get_rent_tile_property()

            if len(property_colors) == [p.property_owner for p in property_colors].count(prop.property_owner):
                # Same owner for every property of that color. If no houses are on that property, double the rent.
                if prop.num_houses == 0:
                    rent *= 2

            return rent

        if prop.tile_type == TileType.RAILROAD:
            # Get all properties of the same type owned by the user who also owns property_name
            num_properties_owned = 0

            for p in Properties.properties:
                if p.tile_type == prop.tile_type and p.property_owner == prop.property_owner:
                    num_properties_owned += 1

            return prop.get_rent_by_owner_count(num_properties_owned)

        if prop.tile_type == TileType.UTILITY:
            # Get all properties of the same type owned by the user who also owns property_name
            num_properties_owned = 0

            for p in Properties.properties:
                if p.tile_type == prop.tile_type and p.property_owner == prop.property_owner:
                    num_properties_owned += 1

            return prop.get_rent_by_owner_count(num_properties_owned, dice_roll)

    @staticmethod
    def get_reference_colors_dict():
        colors = {}
        tile_properties = Properties.properties
        for prop in tile_properties:
            if prop.color not in colors.keys():
                colors[prop.color] = 1
            else:
                colors[prop.color] += 1

        return colors

    @staticmethod
    def get_properties_by_color(color):
        props = []
        for prop in Properties.properties:
            if prop.tile_type == TileType.PROPERTY:
                if prop.color == color:
                    props.append(prop)

        return props
