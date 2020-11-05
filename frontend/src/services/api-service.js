const axios = require('axios').default;

const apiHost = 'localhost:8000';


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
        let regionCount = -1;
        let pageIndex = 1;

        return (async function loop() {
            while (regionList.length !== regionCount) {
                await self.service.get(`${self.baseUrl}${self.routes.regions}?page=${pageIndex}`)
                    .then(function(response) {
                        regionCount = response.data.count;
                        response.data.results.forEach(function(e) {
                            regionList.push(e)
                        });

                        pageIndex += 1;
                    });
            }
        })().then(function() {
            console.log('done');
            return regionList
        });
    }

    listDepartments() {
        let self = this;
        let depList = [];
        let depCount = -1;
        let pageIndex = 1;

        return (async function loop() {
            while (depList.length !== depCount) {
                await self.service.get(`${self.baseUrl}${self.routes.departments}?page=${pageIndex}`)
                    .then(function(response) {
                        depCount = response.data.count;
                        response.data.results.forEach(function(e) {
                            depList.push(e)
                        });

                        pageIndex += 1;
                    });
            }
        })().then(function() {
            console.log('done');
            return depList
        });
    }
}