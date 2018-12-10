<template>
  <form>
    <v-text-field
        v-validate="'required|max:10'"
        v-model="userDetails.name"
        :counter="10"
        :error-messages="errors.collect('name')"
        label="Name"
        data-vv-name="name"
        required
    ></v-text-field>
    {{ name }}
    <v-text-field
        v-validate="'required|email'"
        v-model="userDetails.email"
        :error-messages="errors.collect('email')"
        label="E-mail"
        data-vv-name="email"
        required
    ></v-text-field>
    <v-select
        :items="subjects"
        v-model="userDetails.expertise"
        :menu-props="{ maxHeight: '400' }"
        label="Select your known subjects"
        multiple
    ></v-select>
    {{e6}}
    <v-checkbox
        v-validate="'required'"
        v-model="checkbox"
        :error-messages="errors.collect('checkbox')"
        value="1"
        label="Option"
        data-vv-name="checkbox"
        type="checkbox"
        required
    ></v-checkbox>
    <v-btn @click="submit">submit</v-btn>
    <v-btn @click="clear">clear</v-btn>
    Form Data to send to server:
    {{ userDetails }}
  </form>
</template>

<script>
  export default {
    data () {
      return {
        subjects: ['English', 'Maths', 'Physics'],
        userDetails: {
          name: '',
          email: '',
          expertise: []
        }
      }
    }
  }
</script>
