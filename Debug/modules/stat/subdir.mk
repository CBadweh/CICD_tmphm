################################################################################
# Automatically-generated file. Do not edit!
# Toolchain: GNU Tools for STM32 (12.3.rel1)
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
C:/Users/Sheen/Desktop/Embedded_System/I2C_tmphm/i2c-class-1-code-master/modules/stat/stat.c 

OBJS += \
./modules/stat/stat.o 

C_DEPS += \
./modules/stat/stat.d 


# Each subdirectory must supply rules for building sources it contributes
modules/stat/stat.o: C:/Users/Sheen/Desktop/Embedded_System/I2C_tmphm/i2c-class-1-code-master/modules/stat/stat.c modules/stat/subdir.mk
	arm-none-eabi-gcc "$<" -mcpu=cortex-m4 -std=gnu11 -g3 -DDEBUG -DSTM32F401xE -DUSE_FULL_LL_DRIVER -DHSE_VALUE=8000000 -DHSE_STARTUP_TIMEOUT=100 -DLSE_STARTUP_TIMEOUT=5000 -DLSE_VALUE=32768 -DEXTERNAL_CLOCK_VALUE=12288000 -DHSI_VALUE=16000000 -DLSI_VALUE=32000 -DVDD_VALUE=3300 -DPREFETCH_ENABLE=1 -DINSTRUCTION_CACHE_ENABLE=1 -DDATA_CACHE_ENABLE=1 -c -I../Core/Inc -I../Drivers/STM32F4xx_HAL_Driver/Inc -I../Drivers/CMSIS/Device/ST/STM32F4xx/Include -I../Drivers/CMSIS/Include -I"C:/Users/Sheen/Desktop/Embedded_System/I2C_tmphm/i2c-class-1-code-master/modules/include" -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -fcyclomatic-complexity -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" --specs=nano.specs -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -o "$@"

clean: clean-modules-2f-stat

clean-modules-2f-stat:
	-$(RM) ./modules/stat/stat.cyclo ./modules/stat/stat.d ./modules/stat/stat.o ./modules/stat/stat.su

.PHONY: clean-modules-2f-stat

