import mongoose from "mongoose";

const petSchema = new mongoose.Schema(
  {
    name: {
      type: String,
      required: [true, "Name is required"],
    },
    breed: {
      type: String,
      required: [true, "Breed is required"],
    },
    date_of_birth: {
      type: Date,
    },
    animal_type: {
      type: String,
    },
  },
  {
    timestamps: true,
  }
);

export default mongoose.model("Pet", userSchema);
