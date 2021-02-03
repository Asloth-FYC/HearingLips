<template>
    <div>
        <div class="header">
		<el-button type="text" icon="el-icon-arrow-left"></el-button>
        </div>
        <div class="play">
            <div class="playvideos">
                <video ref='myvideo' :src="url" controls="controls" width="560px" height="378px" >
                    your browser does not support the video tag
                </video>
            </div>
            <div class="fun">
                  <el-tabs v-model="activeName" type="card" class="tab">
                    <el-tab-pane label="编辑字幕" name="first">
                      <subtitle @settime="settime"></subtitle>
                    </el-tab-pane>
                    <el-tab-pane label="功能二" name="second">配置管理</el-tab-pane>
                    <el-tab-pane label="功能三" name="third">角色管理</el-tab-pane>
                  </el-tabs>
            </div>
        </div>
    </div>
</template>

<script>

    import Subtitle from "@/components/subtitle";
    export default {
      components: {Subtitle},
      data(){
        return{
          time: '',
          activeName:'first',
          url:''
        }
      },
      created(){
        this.url = this.$route.params.url;
        console.log(this.url);
      },
      watch:{
        time:function (){
          console.log(this.time)
          this.$refs.myvideo.currentTime=this.time
        }
      },
      methods: {
        settime(time){
          this.time=time
        },
      }
    }
</script>

<style>
.tab{
  background-color: white;
}
    video{
        outline: none
    }
.header{
    margin: 0 40px 0 40px;
    height: 60px;
}
    .play{
        padding-top:40px ;
        /*background-color: rgb(246,246,246);*/
    }
    .playvideos{
        margin:  0 40px 0 40px;
    }
    .fun{
  position: relative;
        left: 640px;
        bottom: 385px;
        width: 670px;
    }
    .header2{
        padding-left: 5px;
        padding-right: 5px;
        line-height: 73px;
        width: 660px;
        height: 73px;
        background-color: rgb(255,255,255);
    }
    .fenjie{
        height: 5px;
    }
    .body2{
        position: relative;
        padding-left: 5px;
        padding-right: 5px;
        width: 660px;
        height: 800px;
        background-color: rgb(255,255,255);

    }
    .pimg{
        position: absolute;
        left: 50%;
        top: 50%;
        transform: translate3d(-50%,-50%,0);
    }
</style>
