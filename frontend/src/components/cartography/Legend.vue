<template>
    <div class="card">
        <div class="card-header">
            <h3>Légende</h3>
        </div>
        <div class="card-body">
            <div style="text-align: center"><strong>{{this.desc}}</strong></div>
            <canvas id="canvas"></canvas>
            <strong>Score :</strong> Score de la commune<br>
            <strong>Score Département :</strong> Score de la commune par rapport au département<br>
            <strong>Score Région :</strong> Score de la commune par rapport à la région<br>
            <strong>Population :</strong> Nombres d'habitants dans la zone<br>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Legend",
        data () {
            return {
                desc: "Score (0 - 276)"
            }
        },
        methods: {
            drawColorMaps (colormap) {
                let c = document.getElementById("canvas").getContext('2d')
                let width = 1
                for (let j = 0; j < 276; j++) {
                    c.fillStyle = colormap[275 - j];      // start ind at index 0
                    c.fillRect(j * width, 10, width, 100);
                }
                c.fillStyle = '#262626';
                c.font = '16px Helvetica';
            }
        },
        mounted () {
            let colormap = require('colormap')
            let colors = colormap({
                colormap: 'YIGnBu',
                nshades: 276,
                format: 'rgbaString',
                alpha: [0.7, 0.9]
            })
            this.drawColorMaps(colors)
        }
    }
</script>

<style scoped>
#canvas {
    height: 40px;
    width: 300px;
}
</style>
