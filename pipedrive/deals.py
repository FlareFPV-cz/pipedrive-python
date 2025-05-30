class Deals:
    def __init__(self, client):
        self._client = client

    async def get_deal(self, deal_id, **kwargs):
        url = "deals/{}".format(deal_id)
        return await self._client._get(self._client.BASE_URL + url, **kwargs)

    async def get_all_deals(self, params=None, **kwargs):
        url = "deals"
        return await self._client._get(self._client.BASE_URL + url, params=params, **kwargs)

    async def get_all_deals_with_filter(self, filter_id, params=None, **kwargs):
        url = "deals?filter_id={}".format(filter_id)
        return await self._client._get(self._client.BASE_URL + url, params=params, **kwargs)

    async def create_deal(self, data, **kwargs):
        url = "deals"
        return await self._client._post(self._client.BASE_URL + url, json=data, **kwargs)

    async def update_deal(self, deal_id, data, **kwargs):
        url = "deals/{}".format(deal_id)
        return await self._client._put(self._client.BASE_URL + url, json=data, **kwargs)

    async def delete_deal(self, deal_id, **kwargs):
        url = "deals/{}".format(deal_id)
        return await self._client._delete(self._client.BASE_URL + url, **kwargs)

    async def duplicate_deal(self, deal_id, **kwargs):
        url = "deals/{}/duplicate".format(deal_id)
        return await self._client._post(self._client.BASE_URL + url, **kwargs)

    async def get_deal_details(self, deal_id, **kwargs):
        url = "deals/{}".format(deal_id)
        return await self._client._get(self._client.BASE_URL + url, **kwargs)

    async def search_deals(self, params=None, **kwargs):
        url = "deals/search"
        return await self._client._get(self._client.BASE_URL + url, params=params, **kwargs)

    async def get_deal_followers(self, deal_id, **kwargs):
        url = "deals/{}/followers".format(deal_id)
        return await self._client._get(self._client.BASE_URL + url, **kwargs)

    async def add_follower_to_deal(self, deal_id, user_id, **kwargs):
        url = "deals/{}/followers".format(deal_id)
        data = {"user_id": user_id}
        return await self._client._post(self._client.BASE_URL + url, json=data, **kwargs)

    async def delete_follower_to_deal(self, deal_id, follower_id, **kwargs):
        url = "deals/{}/followers/{}".format(deal_id, follower_id)
        return await self._client._delete(self._client.BASE_URL + url, **kwargs)

    async def get_deal_participants(self, deal_id, **kwargs):
        url = "deals/{}/participants".format(deal_id)
        return await self._client._get(self._client.BASE_URL + url, **kwargs)

    async def add_participants_to_deal(self, deal_id, person_id, **kwargs):
        url = "deals/{}/participants".format(deal_id)
        data = {"person_id": person_id}
        return await self._client._post(self._client.BASE_URL + url, json=data, **kwargs)

    async def delete_participant_to_deal(self, deal_id, participant_id, **kwargs):
        url = "deals/{}/participants/{}".format(deal_id, participant_id)
        return await self._client._delete(self._client.BASE_URL + url, **kwargs)

    async def get_deal_activities(self, deal_id, **kwargs):
        url = "deals/{}/activities".format(deal_id)
        return await self._client._get(self._client.BASE_URL + url, **kwargs)

    async def get_deal_mail_messages(self, deal_id, **kwargs):
        url = "deals/{}/mailMessages".format(deal_id)
        return await self._client._get(self._client.BASE_URL + url, **kwargs)

    async def get_deal_products(self, deal_id, **kwargs):
        url = "deals/{}/products".format(deal_id)
        return await self._client._get(self._client.BASE_URL + url, **kwargs)

    async def get_deal_fields(self, params=None, **kwargs):
        url = "dealFields"
        return await self._client._get(self._client.BASE_URL + url, params=params, **kwargs)

    async def add_product_to_deal(self, deal_id, data, **kwargs):
        url = "deals/{}/products".format(deal_id)
        return await self._client._post(self._client.BASE_URL + url, json=data, **kwargs)

    async def get_deal_updates(self, deal_id, **kwargs):
        url = "deals/{}/flow".format(deal_id)
        return await self._client._get(self._client.BASE_URL + url, **kwargs)
