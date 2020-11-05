const axios = require('axios').default;

const apiHost = 'vps-2ea52359.vps.ovh.net:8000';


export default class ApiService {
    constructor() {
        this.service = axios.create();

        this.baseUrl = `http://${apiHost}`;

        this.routes = {
            regions: '/regions',
            departments: '/departements',
            cities: '/communes',
            neigh: '/quartiers'
        }
    }

    listRegions() {
        let self = this;
        let regionList = [];
        let regionCount = 0;
        let pageIndex = 1;

        const listRegionCall = function() {
            return self.service.get(`${self.baseUrl}${self.routes.regions}?page=${pageIndex}`)
                .then(function(response) {
                    regionCount = response.data.count;
                    for (let a of response.data.results) {
                        regionList.push(a)
                    }

                    if (regionList.length < regionCount) {
                        pageIndex  += 1;
                        return listRegionCall()
                    }
                })
        };

        return listRegionCall().then(function() {
            return regionList
        })
    }
}