<template>
  <div>
    <div class="videos">
      <!-- 后端交互 -->
<!--      <div class="video" v-for="(video,index)in user.viodes" :key="index" @click="isclick(video.url)" @mouseenter="isshow=!isshow" @mouseleave="isshow=!isshow">-->
<!--        <div class="video-time">{{video.time}}}</div>-->
<!--        <el-card shadow="hover">-->
<!--          <img :src="video.url" class="image">-->
<!--        </el-card>-->
<!--        <div class="video-content">{{video.name}}}</div>-->
<!--        <div class="view">{{video.date}}}</div>-->
<!--        <el-button type="danger" round class="vibutton" @click.stop="deleteitems" v-show="isshow">删除</el-button>-->
<!--      </div>-->
      <div class="video" @mouseenter="isshow=!isshow" @mouseleave="isshow=!isshow" @click="isclick">
        <div class="video-time">13.10</div>
        <el-card shadow="hover">
          <img src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png" class="image">
        </el-card>
        <div class="video-content">This Is Cloaud Break</div>
        <div class="view">13.2k views</div>
        <el-button type="danger" round class="vibutton" @click.stop="deleteitems" v-show="isshow">删除</el-button>
      </div>
      <div class="video" @mouseenter="isshow=!isshow" @mouseleave="isshow=!isshow" @click="isclick">
        <div class="video-time">13.10</div>
        <el-card shadow="hover">
          <img src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png" class="image">
        </el-card>
        <div class="video-content">This Is Cloaud Break</div>
        <div class="view">13.2k views</div>
        <el-button type="danger" round class="vibutton" @click.stop="deleteitems" v-show="isshow">删除</el-button>
      </div>
      <div class="video" @mouseenter="isshow=!isshow" @mouseleave="isshow=!isshow" @click="isclick">
        <div class="video-time">13.10</div>
        <el-card shadow="hover">
          <img src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png" class="image">
        </el-card>
        <div class="video-content">This Is Cloaud Break</div>
        <div class="view">13.2k views</div>
        <el-button type="danger" round class="vibutton" @click.stop="deleteitems" v-show="isshow">删除</el-button>
      </div>
      <div class="video" @mouseenter="isshow=!isshow" @mouseleave="isshow=!isshow" @click="isclick">
        <div class="video-time">13.10</div>
        <el-card shadow="hover">
          <img src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png" class="image">
        </el-card>
        <div class="video-content">This Is Cloaud Break</div>
        <div class="view">13.2k views</div>
        <el-button type="danger" round class="vibutton" @click.stop="deleteitems" v-show="isshow">删除</el-button>
      </div>
      <div class="video" @mouseenter="isshow=!isshow" @mouseleave="isshow=!isshow" @click="isclick">
        <div class="video-time">13.10</div>
        <el-card shadow="hover">
          <img src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png" class="image">
        </el-card>
        <div class="video-content">This Is Cloaud Break</div>
        <div class="view">13.2k views</div>
        <el-button type="danger" round class="vibutton" @click.stop="deleteitems" v-show="isshow">删除</el-button>
      </div>
      <div class="video" @mouseenter="isshow=!isshow" @mouseleave="isshow=!isshow" @click="isclick">
        <div class="video-time">13.10</div>
        <el-card shadow="hover">
          <img src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png" class="image">
        </el-card>
        <div class="video-content">This Is Cloaud Break</div>
        <div class="view">13.2k views</div>
        <el-button type="danger" round class="vibutton" @click.stop="deleteitems" v-show="isshow">删除</el-button>
      </div>
      <div class="video" @mouseenter="isshow=!isshow" @mouseleave="isshow=!isshow" @click="isclick">
        <div class="video-time">13.10</div>
        <el-card shadow="hover">
          <img src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png" class="image">
        </el-card>
        <div class="video-content">This Is Cloaud Break</div>
        <div class="view">13.2k views</div>
        <el-button type="danger" round class="vibutton" @click.stop="deleteitems" v-show="isshow">删除</el-button>
      </div>
      <div class="video" @mouseenter="isshow=!isshow" @mouseleave="isshow=!isshow" @click="isclick">
        <div class="video-time">13.10</div>
        <el-card shadow="hover">
          <img src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png" class="image">
        </el-card>
        <div class="video-content">This Is Cloaud Break</div>
        <div class="view">13.2k views</div>
        <el-button type="danger" round class="vibutton" @click.stop="deleteitems" v-show="isshow">删除</el-button>
      </div>
  </div>
  </div>
</template>

<script>
export default {
  data(){
    return{
      isshow:false
    }
  },
props:{
  user:Object
},
methods:{//跳转到当前video播放界面
  isclick(){
    alert('成功')
  },
  deleteitems(){//用来删除video
    if(window.confirm('确定删除视频吗？')){
      alert('删除成功')
    }
}

}
}
</script>
<style lang="scss">
:root {
  --body-font: "Manrope", sans-serif;
  --body-color: #b3b3b3;
  --body-bg-color: #f2f2f2;
  --theme-bg-color: #fafafa;
  --border-color: #efefef;
  --logo-color: #f13a2f;
  --main-color: #808080;
  --header-bg-color: #fff;
}
.videos {
  display: grid;
  grid-template-columns: repeat(4,1fr);
  grid-column-gap: 20px;
  grid-row-gap: 20px;
}
.video video {
  transition: .4s;
  max-width: 100%;
  display: block;
  border-radius: 4px 4px 0 0;
}
.video {

  overflow: hidden;
  box-shadow: -1px 3px 8px -1px rgba(0, 0, 0, 0.1);
  border-radius: 4px;
  position: relative;
  background-color: var(--header-bg-color);
  cursor: pointer;
  &:hover .video-time {
    opacity: 0;
  }

  &:hover .view {
    padding: 10px;
  }
}
.video-time {
  position: absolute;
  background-color: rgba(0, 0, 0, 0.5);
  padding: 8px;
  border-radius: 15px;
  font-size: 12px;
  color: #fff;
  bottom: 80px;
  right: 6px;
  transition: .3s ease-in;
}
.video-content {
  width: 100%;
  color: var(--main-color);
  padding: 15px 10px 0;
  border-radius: 0 0 4px 4px;
  font-size: 14px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
.view {
  padding: 10px;
  position: relative;
  background-color: var(--header-bg-color);
  z-index: 1;
  font-size: 13px;
  display: inline-block;
}
@media (max-width: 980px) {
  .videos {
    grid-template-columns: 1fr 1fr;
  }
}
@media (max-width: 440px){
  .videos{
    grid-template-columns:1fr;
  }
}
.button{
  float: right
}
.image {

  display: block;
}
.vibutton{
  float: right
}
.el-card{
    width: 200px;
  height: 100px;
}
</style>
