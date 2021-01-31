<template>
  <div class="backgroung">
    <div class="portfoliocard">
      <div class="coverphoto"></div>
      <div class="profile_picture"></div>
      <div class="left_col">
        <div class="followers">
          <div class="follow_count">18,541</div>
          Followers
        </div>
        <div class="following">
          <div class="follow_count">181</div>
          Following
        </div>
      </div>
      <div class="right_col">
<!--        后端-->
<!--        <h2 class="h2name">{{user.username}}</h2>-->
<!--        <h3 class="location">{{user.userlocation}}</h3>-->
        <h2 class="h2name">资本剥削冯</h2>
        <h3 class="location">厕所</h3>
        <div v-show="inshow">
        <ul class="contact_information" >
<!--          <li class="before1"><a class="nostyle" href="https://mail.qq.com/">{{user.usereml}}</a></li>-->
<!--          <li class="before1">{{user.username}}</li>-->
<!--          <li class="before1">{{user.userphone}}</li>-->
          <li class="before1"><a class="nostyle" href="https://mail.qq.com/">feng@qq.com</a></li>
          <li class="before1">封邑城</li>
          <li class="before1">415644565</li>
        </ul>
          <div class="center">
          <el-button type="primary" icon="el-icon-star-off" round @click="Modifydata">修改信息</el-button>
        </div>
      </div>
        <div v-show="!inshow">
          <el-input v-model="cuser.username" placeholder="请输入姓名"></el-input>
          <el-input v-model="cuser.userphone" placeholder="请输入电话" ></el-input>
          <el-input v-model="cuser.usereml" placeholder="请输入Emile" ></el-input>
          <el-input v-model="cuser.userlocation" placeholder="请输入地址" ></el-input>
          <div >
            <el-button type="warning" icon="el-icon-star-off" round @click="changedata">确认修改信息</el-button>
            <el-button type="info" icon="el-icon-message" round @click="Modifydata">返回</el-button>
          </div>
        </div>
        <div >
      </div>

      </div>
    </div>
  </div>
</template>

<script>
export default {
  // props:{
  //   user:Object,
  //   Modifyuser: Function
  // },
  data(){
    return{
    inshow:true,
    cuser:{username:'',
      userphone:'',
      usereml:'',
      userlocation:''
    }
    }
  },
  // mounted() {
  //   this.cuser=this.user
  // },
  methods:{
    Modifydata(){
      this.inshow=!this.inshow;
    },
    changedata(){
      // this.Modifyuser(this.cuser)
      alert('修改成功')
      this.inshow=!this.inshow
    }
  }
}
</script>

<style >
.backgroung{
  height:1000px ;
padding-top: 1px;
  background-image: url('https://tse2-mm.cn.bing.net/th/id/OIP.p0ECuqeqIKYPvN3WnrEQmQHaED?w=315&h=180&c=7&o=5&dpr=1.4&pid=1.7');
  background-size:100% 100%;
  font-family:"Open Sans", sans-serif;
}
a.nostyle{
  color:inherit;
  text-decoration:none;
  padding:0;
  margin:0;
}
div.portfoliocard{

  position:relative;
  height:600px;
  width:500px;
  background:rgba(255,255,255,1);
  border:1px solid rgba(0,0,0,0.7);
  box-shadow:0px -1px 3px rgba(0,0,0,0.1),
  0px 2px 6px rgba(0,0,0,0.5);
  border-radius:6px;
  margin:10% auto;
  overflow:hidden;
  z-index:100;
}
div.portfoliocard div.coverphoto{
  width:100%;
  height:120px;
  background:url('http://farm8.staticflickr.com/7149/6484148411_baf8d2e934_z.jpg');
  background-position:center center;
  border-top-right-radius:5px;
  border-top-left-radius:5px;
  border-bottom:1px solid rgba(0,0,0,0.1);
  box-shadow:inset 0px 3px 20px rgba(255,255,255,0.3),
  1px 0px 2px rgba(255,255,255,0.7);
  z-index:99;
}
div.portfoliocard div.left_col, div.portfoliocard div.right_col{
  float:left;
  height:340px;
}
div.portfoliocard div.left_col{
  width:40%;
  padding-top:85px;
  box-sizing:border-box;
}
div.portfoliocard div.right_col{
  width:60%;
  background:rgba(245,245,245,1);
  border-left:1px solid rgba(230,230,230,1);
  box-shadow:inset 0px 1px 1px rgba(255,255,255,0.7);
  margin-left:-1px;
  border-bottom-right-radius:5px;
}
div.portfoliocard div.profile_picture{
  width:110px;
  height:110px;
  background:rgba(255,255,255,1);
  position:absolute;
  top:65px;
  left:40px;
  border-radius:100%;
  background-image: url('http://cache.spreadshirt.net/Public/Common/images/profile-pic-placeholder_130x130.png');
  background-size:100% 100%;
  padding:7px;
  border:4px solid rgba(255,255,255,1)
}
div.portfoliocard div.right_col h2.h2name{
  font-size:30px;
  font-weight:300;
  color: rgba(30,30,30,1);
  padding:0;
  margin:20px 10px 0px 30px;
}
div.portfoliocard div.right_col h3.location{
  font-size:15px;
  font-weight:300;
  color:rgba(170,170,170,1);
  padding:0;
  margin:-5px 10px 10px 30px;
}
div.portfoliocard ul.contact_information{
  margin-top:20px;
  padding-left:30px;
  list-style-type:none;
}
div.portfoliocard ul.contact_information li{
  height:25px;
  width:180px;
  line-height:25px;
  font-weight:300;
  font-size:15px;
  color:rgba(140,140,140,1);
  text-shadow:1px 1px 1px rgba(255,255,255,0.8);
  padding:5px 0px;
  background-repeat:no-repeat;
  background-size:18px 18px;
  border-bottom:1px solid rgba(0,0,0,0.1);
  box-shadow:0px 1px 1px rgba(255,255,255,0.6);
  cursor:default;
}
div.portfoliocard ul.contact_information .before1:before{
  content:"";
  width:25px;
  height:25px;
  display:block;
  float:left;
  background-position:center;
  background-size:18px 18px;
  background-repeat:no-repeat;
  margin-right:5px;
  opacity:0.7;
}
div.portfoliocard div.followers, div.portfoliocard div.following{
  margin:15px 0px 0px 35px;
  font-weight:300;
  font-size:16px;
  color:rgba(30,30,30,1);
}
div.portfoliocard div.follow_count{
  font-weight:400;
  font-size:25px;
  color:rgba(140,140,140,1);
}
div.center{
  text-align: center;
}

</style>
