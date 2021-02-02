const dialogmixin = {
    data() {
        return {
            dialogVisible: false,
        }
    },
    methods: {
        onShow() {
               this.dialogVisible = true;
        },
        onCancel() {
            this.dialogVisible = false;
        },
    }
}
export default dialogmixin