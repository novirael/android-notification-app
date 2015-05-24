#!/usr/bin/env python
# -*- coding: utf-8 -*-

from api.ids import CAR_CATEGORY_ID
from api.utils import memoize
from api.webapi import AllegroWebAPI


class AllegroEndpoints(AllegroWebAPI):

    @memoize
    def _get_all_categories(self):
        """
        Returns all categories found with webapi
        """
        data = self.doGetCatsData()
        return data.catsList.item

    def _get_categories(self, category_id):
        """
        Returns list of subcategories
        :return: [
        {
            name: 'Osobowe',
            id: 1
        },
        {
            name: 'Ciezarowe',
            id: 2
        }]
        """
        car_categories = []

        for category in self._get_all_categories():
            if category.catParent == category_id:
                car_categories.append({
                    'name': unicode(category.catName),
                    'id': category.catId
                })

        return car_categories

    def get_car_categories(self):
        """
        Returns list of car categories
        """
        return self._get_categories(CAR_CATEGORY_ID)

    def _get_items_from_category(self, category_id):
        """
        Returns all items by given category found with webapi
        """
        data = self.service.doShowCat(
            sessionHandle=self.session_id,
            catId=category_id
        )
        return data.catItemsArray.item

    def get_all_car_items(self):
        """
        Returns list of car items
        :return: [
        {
            name: 'Ford nowy ...',
            price: 12000,
            city: Kutno,
            details: {},
            thumbnail: '/url/to/thumbnail'
        },
        {
            name: 'Mercedes',
            price: 25000,
            city: Gdynia,
            details: {},
            thumbnail: '/url/to/thumbnail'
        }]
        """
        new_items = []

        for item in self._get_items_from_category(CAR_CATEGORY_ID):
            details = {}
            # Get item details doesn't work because UnicodeEncodeError
            # details = {
            #     unicode(elem.attribName): [
            #         unicode(attrib)
            #         for attrib in elem.attribValues
            #     ] for elem in item.sItAttribsList.item
            # }

            new_items.append({
                'name': unicode(item.sItName),
                'price': item.sItBuyNowPrice,
                'city': unicode(item.sItCity),
                'details': details,
                'thumbnail': item.sItThumbUrl
            })

        return new_items
