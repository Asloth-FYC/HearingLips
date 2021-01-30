<template>
<div id="container">
    <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
        <el-menu-item index="1">视频</el-menu-item>
        <el-menu-item index="2">音频</el-menu-item>
        <el-menu-item index="3">字幕</el-menu-item>
        <el-menu-item index="4">文档</el-menu-item>
        <el-menu-item index="5" id="btn" >
            <el-button type="primary" plain icon="el-icon-plus" @click="start">新建项目</el-button>
        </el-menu-item>
    </el-menu>
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
</style>

<script>
export default {
    name:'Nav',
    data() {
      return {
        activeIndex: '1',
      };
    },
    methods: {
      handleSelect(key, keyPath) {
        console.log(key, keyPath);
      },
      start(){
        this.$router.push({name:'videoTrans'})
      }
    }
  }
</script>