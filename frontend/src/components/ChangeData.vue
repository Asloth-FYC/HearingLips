<template>
    <el-dialog
            title="忘记密码"
            :visible.sync="dialogVisible"
            :lock-scroll="false"
            width="800px"
            ref="ChangeData">
        <el-form :model="form" ref="form" size="medium" label-width="80px" :rules="rules">
            <el-form-item label="邮箱" prop="email">
                <el-input placeholder="请输入邮箱地址" v-model="form.email"
                          oninput="value=value.replace(/[^\dA-Za-z@.]/g,'')"></el-input>
            </el-form-item>
            <el-form-item label="原密码" prop="inputOpassword" :error="errorText">
                <el-input placeholder="请输入原密码" type="password" maxlength="8"
                          v-model="form.inputOpassword"  ></el-input>
            </el-form-item>
            <el-form-item label="密码" prop="inputPassword" :error="errorText">
                <el-input placeholder="请输入密码" type="password" maxlength="8"
                          v-model="form.inputPassword"  @input="onPasswordInput"></el-input>
            </el-form-item>
            <el-form-item label="确认" prop="confirmPassword" :error="errorText">
                <el-input placeholder="请再次输入密码" type="password" maxlength="8"
                          v-model="form.confirmPassword"  @input="onPasswordInput"></el-input>
            </el-form-item>
            <el-form-item class="text-center">
                <el-button type="primary" @click="onConfirm" style="width: 200px">{{btnText2}}</el-button>
            </el-form-item>
        </el-form>
    </el-dialog>
</template>

<script>
    import dialogmixin from "./dialogMixin";
    import { apiAdminForgetMail, apiAdminForgetPassword} from "../api/admin";
    import md5 from 'js-md5'

    export default {
        mixins: [dialogmixin],
        data() {
            return {
                form: {},
                errorText: '',
                btnText2:'确认',
                rules,
            }
        },
        methods:{
            onPasswordInput(val) {
                if (this.form.inputPassword !== this.form.confirmPassword) {
                    this.errorText = '两次密码不一致';
                } else {
                    this.errorText = '';
                }
            },
            onConfirm() {
                this.$refs.form.validate(valid => {
                    if (valid) {
                        if (this.form.inputPassword !== this.form.confirmPassword) {
                            this.errorText = '两次密码不一致';
                            return;
                        } else {
                            this.errorText = '';
                        }
                        this.$set(this.form, 'password', md5(this.form.username + this.form.inputPassword))
                        apiAdminForgetPassword(this.form).then(() => {
                            this.onCancel();
                        })
                    }
                })
            },
        }
    }
    const emptyText="不能为空";
    var emptyValid = msg => {
        return {required: true, message: msg + emptyText, trigger: "blur"};
    };
    var validateEmail = (rule, value, callback) => {
        if (value) {
            let reg = /^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$/;
            if (!reg.test(value)) {
                callback(new Error("邮箱地址不合法！"));
            }
        }
        callback();
    };
    const rules = {
        inputOpassword:[emptyValid("原密码")],
        inputPassword: [emptyValid("密码")],
        confirmPassword: [emptyValid("确认密码")],
        email: [emptyValid("邮箱"), {validator: validateEmail, trigger: 'blur'}],
    }
</script>

<style scoped>

</style>