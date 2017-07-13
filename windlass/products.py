#!/bin/env python3
#
# (c) Copyright 2017 Hewlett Packard Enterprise Development LP
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#

import windlass.images
import logging
import os.path
import yaml


class Products(object):

    def __init__(self, products_to_parse=[]):
        self.items = []
        self.data = {}
        self.load(products_to_parse)

    def __iter__(self):
        for item in self.items:
            yield item

    def load(self, products_to_parse=[]):
        for product_file in products_to_parse:
            if not os.path.exists(product_file):
                logging.debug(
                    'Products file %s does not exist, skipping' % (
                        product_file))
                continue

            with open(product_file, 'r') as f:
                product_def = yaml.load(f.read())

            # TODO(kerrin) this is not a deep merge, and is pretty poor.
            # Will lose data on you.
            self.data.update(product_def)

            if 'images' in product_def:
                for image_def in product_def['images']:
                    self.items.append(windlass.images.Image(image_def))

#            if 'charts' in product_def:
#                for chart_def in product_def['charts']:
#                    self.charts.append(windlass.charts.Chart(chart_def))
