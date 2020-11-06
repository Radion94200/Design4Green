<template>
    <div class="card">
        <div class="card-header">
            <h3>Recherche</h3>
        </div>
        <div class="card-body">
            <div class="input-group-menu">
                <label for="view-select">Choisissez votre échelle</label>
                <select v-model="view" id="view-select" class="custom-select" disabled>
                    <option :value="views.filterRegion" selected>Région</option>
                    <option :value="views.filterDeps">Département</option>
                    <option :value="views.filterCities">Commune</option>
                </select>
            </div>

            <div class="input-group-menu" v-if="view === views.filterRegion">
                <label for="region-input">Région</label>
                <input v-model="regionInput" type="text" class="form-control" id="region-input">
                <div class="search-results">
                    <div class="search-result" v-for="r of regionSearch" :key="r.id">
                            <span @click="setRegionInput(r.nom)">
                                {{r.nom}}
                            </span>
                    </div>
                </div>
            </div>

            <div class="input-group-menu" v-if="view === views.filterDeps">
                <label for="dep-input">Départment</label>
                <input v-model="depInput" type="text" class="form-control" id="dep-input">
                <div class="search-results">
                    <div class="search-result" v-for="d of depSearch" :key="d.id">
                            <span @click="setDepInput(d.nom)">
                                {{d.nom}}
                            </span>
                    </div>
                </div>
            </div>

            <div class="input-group-menu" v-if="view === views.filterCities">
                <label for="city-input">Commune</label>
                <input @change="searchCity" v-model="cityInput" type="text" class="form-control" id="city-input">
                <div class="search-results">
                    <div class="search-result" v-for="c of cityResults.slice(0, 4)" :key="c.id">
                        <div @click="setCityInput(c.nom)">
                            <span>
                                {{c.nom}}
                            </span>
                        </div>
                    </div>
                </div>
            </div>

            <div class="input-group-menu">
                <button class="btn btn-primary" style="width: 100%" @click="submit">Envoyer</button>
            </div>
        </div>
    </div>
</template>

<script>
    import ApiService from "@/services/api-service";

    export default {
        name: "Filters",
        data() {
            return {
                // service
                service: null,

                // input
                regionInput: "",
                depInput: "",
                cityInput: "",

                // data
                regionList: [],
                depList: [],
                cityResults: [],

                // dom
                views: {
                    filterRegion: 'filterRegion',
                    filterDeps: 'filterDeps',
                    filterCities: 'filterCities'
                },
                view: 'filterCities'
            };
        },
        mounted() {
            this.service = new ApiService();

        },
        computed: {
            regionSearch: function() {
                let self = this;
                if (self.regionInput === "") {
                    return []
                } else {
                    let dl = [];
                    for (let i = 0; i < this.regionList.length; i++) {
                        let r = this.regionList[i];
                        if (r.nom === self.regionInput) {
                            return []
                        }

                        let re = new RegExp(self.regionInput.toUpperCase());
                        if (r.nom.match(re)) {
                            dl.push(r)
                        }

                        if (dl.length === 5) {
                            return dl;
                        }
                    }

                    return dl;
                }
            },
            depSearch: function() {
                let self = this;
                if (self.depInput === "") {
                    return []
                } else {
                    let dl = [];
                    for (let i = 0; i < this.depList.length; i++) {
                        let d = this.depList[i];
                        if (d.nom === self.depInput) {
                            return []
                        }

                        let re = new RegExp(self.depInput.toUpperCase());
                        if (d.nom.match(re)) {
                            dl.push(d)
                        }

                        if (dl.length === 5) {
                            return dl;
                        }
                    }

                    return dl;
                }

            }
        },
        methods: {
            async submit() {
                const res = await this.service.getCity(this.cityInput)
                if (res.length === 1) {
                    this.$emit("recherche", res[0])
                }
            },

            listRegions() {
                let self = this;

                this.service.listRegions()
                    .then(function(r) {
                        self.regionList = r;
                    });
            },

            listDep() {
                let self = this;
                this.service.listDepartments()
                    .then(function(d) {
                        self.depList = d;
                    })
            },

            searchCity() {
                let self = this;

                if (self.cityInput === "") {
                    self.cityResults = [];
                    return
                }
                this.service.searchCity(self.cityInput)
                    .then(function(rl) {
                        self.cityResults = rl;
                    })
            },

            setRegionInput(reg) {
                this.regionInput = reg;
            },

            setDepInput(dep) {
                this.depInput = dep;
            },

            setCityInput(city) {
                this.cityInput = city;
                this.cityResults = [];
            }
        }

    }
</script>

<style scoped>
    .search-results {
        width: 86%;
        position: absolute;
        text-align: center;
    }

    .search-result {
        border-bottom: solid 1px black;
        border-left: solid 1px black;
        border-right: solid 1px black;
        background-color: white;

        cursor: pointer;
    }

    .search-result:hover {
        background-color: lightgrey;
    }

    .input-group-menu {
        margin-top: 10px;
        margin-bottom: 10px;
        width: 100%;
    }

</style>
