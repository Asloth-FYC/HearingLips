<template>
<!--  <input type="text" v-model='time' @input="toParent"></input>-->
  <div class="block">
    <el-timeline>
      <el-timeline-item v-for="sentence in sentences"
                        :timestamp="sentence.stime"
                        placement="top">
        <div @click="chooseTime(sentence.stime)" class="sentence">
          <el-card >
            <p>{{sentence.msg}}</p>
          </el-card>
        </div>
      </el-timeline-item>
    </el-timeline>
  </div>

</template>

<script>
export default {
  name: "subtitle",
  data(){
    return{
      time:'',
      sentences:[
        {stime:'0',msg:'录屏开始'},
        {stime:'1',msg:'xxxxxxxxxxx'},
        {stime:'3',msg:'yyyyyyyyyyyyyyyy'},
        {stime:'4',msg:'yyyyyyyyyyyyyyyy'}
      ]
    }
  },
  watch:{
    time:function (){
      this.toParent()
    }
  },
  methods:{
    toParent() {
      this.$emit('settime', this.time)
    },
    chooseTime(time){
      console.log(time);
      this.time=time
    }
  }
}
</script>

<style scoped>
.sentence{
  display: block;
}
</style>