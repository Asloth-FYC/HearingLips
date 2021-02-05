<template>
<div>
    <div>
        <router-link to="/">
            <strong style="font: italic 1.3em Georgia, serif;">HearingLips</strong>
        </router-link>
        <el-dropdown>
            <el-button icon="el-icon-user" circle></el-button>
            <el-dropdown-menu slot="dropdown">
                <router-link to="/profile">
                <el-dropdown-item v-if="signed">
                    <span>Signed in as</span>
                    <strong style="display:block;">{{this.username}}<i class="el-icon-edit"></i></strong>
                </el-dropdown-item>
                </router-link>
                <el-dropdown-item divided @click.native="change">
                    修改密码
                </el-dropdown-item>
            <router-link to="/">
                <el-dropdown-item divided>项目介绍</el-dropdown-item>
            </router-link>
            <a target="_blank" href="https://github.com/Asloth-FYC/HearingLips">
                <el-dropdown-item>Github</el-dropdown-item>
            </a>
            <el-dropdown-item divided @click.native="logout">
                <span style="display:block;"><span v-if="signed">退出</span>登录</span>
            </el-dropdown-item>
            </el-dropdown-menu>
        </el-dropdown>
        <ChangeData ref="ChangeData"></ChangeData>
    </div>
</div>
    
</template>

<style scoped>
.el-dropdown {
    vertical-align: top;
    position: absolute;
    right: 20px;
}
a {
  text-decoration: none;
}

</style>

<script>
import ChangeData from "./ChangeData";
export default {
    name:'Header',
    components:{ChangeData},
    props:{
        signed:Boolean,
        username:String
    },
    methods:{
        logout() {
            if(this.signed){
                localStorage.removeItem('Authorization');
            }
            this.$router.push({name:'login'})
        },
        change(){
            this.$refs.ChangeData.onShow();
        }
    }
}
</script>