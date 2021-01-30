<template>
<div id="container">
    <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
        <el-menu-item index="1">视频</el-menu-item>
        <el-menu-item index="2">音频</el-menu-item>
        <el-menu-item index="3">字幕</el-menu-item>
        <el-menu-item index="4">文档</el-menu-item>
        <el-menu-item index="5" id="btn" >
            <el-button type="primary" plain icon="el-icon-plus" @click="dialogUploaderVisble=true">新建项目</el-button>
        </el-menu-item>
    </el-menu>
    <el-dialog top=10% class="uploaderDialog"  :visible.sync="dialogUploaderVisble">
      <Uploader></Uploader>
    </el-dialog>
</div>
</template>

<style scoped>
.el-menu-demo{
    width: 70%;
    margin:auto;
}
#btn{
    position:absolute; 
    right:0;
}
.uploaderDialog{
  width:auto;
}
</style>

<script>
import Uploader from "@/components/Uploader";
export default {
    name:'Nav',
    data() {
      return {
        activeIndex: '1',
        dialogUploaderVisble:false
      };
    },
    methods: {
      handleSelect(key, keyPath) {
        console.log(key, keyPath);
      }
    },
    components:{
      Uploader
    }
  }
</script>