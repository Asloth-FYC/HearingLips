<template>
    <el-card shadow="hover" class="card">
        <div class="title-wrapper f-cb">
            <span><i class="el-icon-video-camera"></i></span> 
            <div class="title">{{project_name}}</div>
        </div>
        <div class="image-wrapper" @click="isclick">
            <img src="?imageView&amp;thumbnail=210y110"> 
            <span class="duration">00:03</span> 
        </div>
        <div class="ft">
            <span class="time">{{create_at}}</span> 
            <el-popconfirm title="确定删除此视频？">
                <el-button plain icon="el-icon-delete" circle class="remove" size="mini" slot="reference"></el-button>
            </el-popconfirm>
        </div>
    </el-card>
</template>
<script>
    export default {
        props:{
            create_at:String,
            project_name:String,
            url:String
        },
        methods:{
            isclick(){
                this.$router.push({
                    name:'play',
                    params:{url:this.url}
                })
            }
        }
    }
</script>
<style scoped lang="scss">
.card{
    display: inline-block;
    width: 240px;
    height: 240px;
    margin: 0 20px 20px 0;
    padding-right: 10px;
    background: #fff;
    border-radius: 2px;
    &:hover .duration {
     opacity: 0;
 }
    &:hover .remove {
        opacity: 100;
    }

}
.card .image-wrapper img{
    display: inline-block;
    width: 210px;
    height: 110px;
    cursor: pointer;
}
.title-wrapper{
    height: 44px;
}
.title{
    float: right;
    width: 180px;
    color: #2b2e3e;
    font-weight: bold;
    font-size: 16px;
    word-break: break-all;
}
.card .image-wrapper{
    position: relative;
    height: 110px;
    margin-top: 20px;
}
.card .image-wrapper .duration{
    position: absolute;
    right: 0;
    bottom: 10px;
    min-width: 40px;
    height: 20px;
    padding: 0 5px;
    color: #fff;
    font-size: 12px;
    line-height: 20px;
    text-align: center;
    background: rgba(0, 0, 0, 0.5);
    border-radius: 2px;
}
.card .ft{
    position: relative;
    height: 32px;
}
.card .ft .time{
    position: absolute;
    top: 12px;
    left: 0;
    color: #999;
    font-size: 12px;
}
.card .ft .icon-remove{
    position: absolute;
    top: 14px;
    right: 0;
    display: none;
    width: 14px;
    height: 14px;
    cursor: pointer;
}
.remove{
    position: absolute;
    top: 10px;
    right: 0;
    opacity: 0;
}
    .duration{
        transition: .3s ease-in;

    }
</style>