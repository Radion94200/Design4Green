const axios = require('axios').default;

const apiHost = 'http://vps-2ea52359.vps.ovh.net:8000';


export default class ApiService {
    constructor() {
        this.service = axios.create();

        this.baseUrl = apiHost;

        this.routes = {
            regions: '/regions',
            departments: '/departements',
            cities: '/communes',
            neigh: '/quartiers',
            geojson: '/geojson'
        }
    }

    listPaging(route, ) {
        let self = this;
        let l = [];
        let c = -1;
        let pageIndex = 1;

        return (async function loop() {
            while (l.length !== c) {
                await self.service.get(`${self.baseUrl}${route}?page=${pageIndex}`)
                    .then(function(response) {
                        c = response.data.count;
                        response.data.results.forEach(function(e) {
                            l.push(e)
                        });

                        pageIndex += 1;
                    });
            }
        })().then(function() {
            return l
        });
    }

    listRegions() {
        return this.listPaging(this.routes.regions)
    }

    listDepartments() {
        return this.listPaging(this.routes.departments)
    }

    searchCity(query) {
        return this.service.get(`${this.baseUrl}${this.routes.cities}`, {
            params: {
                search: query
            }
        }).then(function(res) {
            return res.data.results
        })
    }

    getCity(query) {
        return this.service.get(`${this.baseUrl}${this.routes.cities}`, {
            params: {
                nom: query
            }
        }).then(function(res) {
            return res.data.results
        })
    }
}
