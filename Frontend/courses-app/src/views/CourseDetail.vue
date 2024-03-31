<template>
    <div class="container">
        <div class="mb-4">
            <navbar/>
        </div>
        <detail/>
    </div>
</template>

<style>

</style>

<script>
import detail from '@/components/detail.vue'
import navbar from '@/components/navbar.vue'
export default {
    name:'course detail',
    components:{
        detail,
        navbar,
    }
}
</script>