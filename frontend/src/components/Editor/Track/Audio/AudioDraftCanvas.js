import DraftCanvasMixin from '../DraftCanvasMixin.js';

export default {
  name: 'AudioDraftCanvas',
  mixins: [DraftCanvasMixin],
  props: ['sourceNode'],
  created(){
    this.analyserNode = this.sourceNode.context.createAnalyser();
    this.analyserNode.fftSize = 1024;
    this.sourceNode.connect(this.analyserNode);
    this.dataArray = new Float32Array(this.analyserNode.fftSize);
  },
  unmounted(){
    this.sourceNode.disconnect(this.analyserNode);
  },
  computed: {
    slice_width(){
      return this.$store.getters.animation_width / this.dataArray.length;
    }
  },
  methods: {
    initCtxStyle(){
      this.ctx.fillStyle = "#78328c";
      this.ctx.lineWidth = 2;
      this.ctx.strokeStyle = "#000";
    },

    draw(){
      if(this.drawPoint >= this.canvas.width){
        this.resize();
      }

      this.analyserNode.getFloatTimeDomainData(this.dataArray);

      this.ctx.fillRect(
        this.drawPoint,
        0,
        this.$store.getters.animation_width,
        this.canvas.height
      );

      this.ctx.beginPath();
      for (let i = 0; i < this.dataArray.length; i++) {
        let y = (this.dataArray[i] + 1) * this.canvas.height / 2;

        if (i === 0) {
          this.ctx.moveTo(this.drawPoint, y);
        } else {
          this.ctx.lineTo(this.drawPoint, y);
        }
        this.drawPoint += this.slice_width;
      }
      this.ctx.stroke();
    }
  }
}
