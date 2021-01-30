<template>
<div>
    <div>
        <router-link to="/">
            <strong style="font: italic 1.3em Georgia, serif;">HearingLips</strong>
        </router-link>
        <el-dropdown>
            <el-button icon="el-icon-user" circle></el-button>
            <el-dropdown-menu slot="dropdown">
                <router-link to="/profile/index">
                <el-dropdown-item v-if="signed">
                    <span>Signed in as</span>
                    <strong style="display:block;">{{this.$cookies.get('user')}}<i class="el-icon-edit"></i></strong>
                </el-dropdown-item>
                </router-link>
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
export default {
    name:'Header',
    props:{
        signed:Boolean
    },
    methods:{
        logout() {
            if(this.signed){
                this.$cookies.remove('user')
            }
            this.$router.push({name:'login'})
        }
    },
}
</script>