<template>
<!--  <input type="text" v-model='time' @input="toParent"></input>-->
  <div class="block">
    <el-timeline>
      <el-timeline-item v-for="sentence in sentences"
                        :timestamp="sentence.showTime"
                        placement="top">
        <div @click="chooseTime(sentence.stime)" class="sentence">
          <el-card >
            <el-input type="textarea"
                      autosize
                      v-model="sentence.msg"></el-input>
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
        {stime:'0',showTime:'00:00',msg:'录屏开始'},
        {stime:'1',showTime:'00:01',msg:'xxxxxxxxxxx'},
        {stime:'3',showTime:'00:03',msg:'yyyyyyyyyyyyyyyy'},
        {stime:'4',showTime:'00:04',msg:'yyyyyyyyyyyyyyyy'}
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
el-input{
  border:0px;
  outline:none;
}
.sentence{
  display: block;
}
</style>