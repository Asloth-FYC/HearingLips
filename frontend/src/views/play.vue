<template>
    <div>
        <div class="header">
		<el-button type="text" icon="el-icon-arrow-left"></el-button>
        </div>
        <div class="play">
            <div class="playvideos">
                <video src="../assets/img/video.mp4" controls="controls" width="560px" height="378px" >
                    your browser does not support the video tag
                </video>
            </div>
            <div class="fun">
                <div class="header2">
                    <el-button >功能一</el-button>
                    <el-button >功能二</el-button>
                    <el-button >功能三</el-button>
                </div>
                <div class="fenjie" >

                </div>
                <div class="body2">
                    <img src="https://jianwai.youdao.com/assets/img/no-card.20208f4.png" alt="无法显示图片" class="pimg">
                </div>
    </div>
    </div>
    </div>
</template>

<script>
    export default {}
</script>

<style>
    video{
        outline: none
    }
.header{
    margin: 0 40px 0 40px;
    height: 60px;
}
    .play{
        padding-top:40px ;
        background-color: rgb(246,246,246);
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
